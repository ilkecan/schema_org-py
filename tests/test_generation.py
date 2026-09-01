from pathlib import Path

import pytest
from schema_org_codegen import Vocabulary
from schema_org_codegen.generator import _ordered_direct_parents, generate

from schema_org import (
    AmpStory,
    Course,
    Dentist,
    InteractionCounter,
    MedicalAudience,
    Observation,
    Offer,
    PalliativeProcedure,
    SequentialArt,
    TVSeason,
    TVSeries,
    registry,
)
from schema_org.base import ClassMetadata, PropertyMetadata


@pytest.mark.parametrize(
    ("model", "parents"),
    [
        (AmpStory, ("MediaObject", "CreativeWork")),
        (Course, ("LearningResource", "CreativeWork")),
        (Dentist, ("MedicalBusiness", "LocalBusiness", "MedicalOrganization")),
        (MedicalAudience, ("PeopleAudience", "Audience")),
        (Observation, ("QuantitativeValue", "Intangible")),
        (PalliativeProcedure, ("MedicalTherapy", "MedicalProcedure")),
        (TVSeason, ("CreativeWorkSeason", "CreativeWork")),
        (TVSeries, ("CreativeWorkSeries", "CreativeWork")),
        (SequentialArt, ("Book", "VisualArtwork")),
    ],
)
def test_direct_bases_preserve_schema_parents(model, parents):
    assert tuple(base.__name__ for base in model.__bases__) == parents
    assert all(issubclass(model, base) for base in model.__bases__)


def test_generated_metadata_is_frozen_and_complete():
    assert ClassMetadata.__dataclass_params__.frozen
    assert PropertyMetadata.__dataclass_params__.frozen
    assert isinstance(registry.CLASS_METADATA["SequentialArt"], ClassMetadata)
    assert all(isinstance(value, PropertyMetadata) for value in SequentialArt.SCHEMA_PROPERTIES)


def test_supersession_metadata_and_descriptions_are_complete():
    predecessors = (
        "UserBlocks",
        "UserCheckins",
        "UserComments",
        "UserDownloads",
        "UserInteraction",
        "UserLikes",
        "UserPageVisits",
        "UserPlays",
        "UserPlusOnes",
        "UserTweets",
    )
    assert registry.CLASS_METADATA["InteractionCounter"].supersedes == predecessors
    assert registry.PROPERTY_BY_SCHEMA["seller"].supersedes == ("merchant", "vendor")
    assert all(
        registry.CLASS_METADATA[name].superseded_by == "InteractionCounter"
        for name in predecessors
    )
    assert all(f"Supersedes `{name}`." in InteractionCounter.__doc__ for name in predecessors)
    seller_description = Offer.model_fields["seller"].description
    assert seller_description is not None
    assert seller_description.index("Supersedes `merchant`.") < seller_description.index(
        "Supersedes `vendor`."
    )


def test_c3_ordering_is_deterministic(tmp_path: Path):
    ttl = (
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
        "schema:A a rdfs:Class ; rdfs:label \"A\" ; rdfs:subClassOf schema:Thing .\n"
        "schema:B a rdfs:Class ; rdfs:label \"B\" ; rdfs:subClassOf schema:Thing .\n"
        "schema:C a rdfs:Class ; rdfs:label \"C\" ; rdfs:subClassOf schema:A, schema:B .\n"
    )
    schema = tmp_path / "schema.ttl"
    schema.write_text(ttl, encoding="utf-8")
    assert _ordered_direct_parents(Vocabulary.from_file(schema), "C") == ("A", "B")
    generate(schema, project_root=tmp_path, output_root=tmp_path)
