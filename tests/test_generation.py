import json
from pathlib import Path
from types import MappingProxyType

import pytest
from schema_org_codegen import Vocabulary
from schema_org_codegen.generator import _ordered_direct_parents, generate

from schema_org import (
    AmpStory,
    APIReference,
    ArchiveComponent,
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



def test_manifest_and_generated_metadata_are_complete():
    root = Path(__file__).parents[1]
    vocabulary = Vocabulary.from_file(root / "codegen/data/schema.ttl")
    manifest = json.loads((root / "codegen/generated_manifest.json").read_text())
    assert manifest["terms"] == {
        "classes": sorted(subject.name for subject in vocabulary.classes),
        "datatypes": sorted(subject.name for subject in vocabulary.datatype_classes),
        "enumerations": sorted(subject.name for subject in vocabulary.enumeration_classes),
        "enumeration_members": sorted(member.name for member in vocabulary.enumeration_members),
        "properties": sorted(subject.name for subject in vocabulary.properties),
    }
    expected_paths = {
        "src/schema_org/__init__.py",
        "src/schema_org/datatypes.py",
        "src/schema_org/enums.py",
        "src/schema_org/registry.py",
        "src/schema_org/schema_version.py",
        "src/schema_org/py.typed",
        "src/schema_org/models/__init__.py",
    }
    from schema_org_codegen.naming import module_name

    expected_paths.update(
        f"src/schema_org/models/{module_name(subject.name)}.py"
        for subject in vocabulary.ordinary_classes
    )
    assert manifest["paths"] == sorted(expected_paths)
    assert isinstance(registry.CLASS_METADATA, MappingProxyType)
    assert isinstance(registry.PROPERTY_BY_SCHEMA, MappingProxyType)
    assert isinstance(registry.ENUM_MEMBER_METADATA, MappingProxyType)
    for metadata in registry.CLASS_METADATA.values():
        assert isinstance(metadata.parents, tuple)
        assert isinstance(metadata.properties, tuple)
    for metadata in registry.PROPERTY_BY_SCHEMA.values():
        assert isinstance(metadata.ranges, tuple)
        assert isinstance(metadata.domains, tuple)
        assert isinstance(metadata.supersedes, tuple)
    for metadata in registry.ENUM_MEMBER_METADATA.values():
        assert isinstance(metadata.types, tuple)
    assert (
        ArchiveComponent.model_fields["holding_archive"].description
        == "[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].\n\n"
        "Inverse-property: `archiveHeld`."
    )
    assert "Library file name, e.g., mscorlib.dll, system.web.dll." in (
        APIReference.model_fields["assembly"].description or ""
    )
    assert "Superseded by `executableLibraryName`." in (
        APIReference.model_fields["assembly"].description or ""
    )


def test_provenance_has_only_ruby_headers_and_schema_version(tmp_path: Path):
    root = Path(__file__).parents[1]
    ttl_lines = (root / "codegen/data/schema.ttl").read_text().splitlines()
    assert ttl_lines[:2] == [
        "# schema_org_release: v30.0",
        "# schema_org_source: https://schema.org/version/30.0/schemaorg-all-https.ttl",
    ]
    manifest = json.loads((root / "codegen/generated_manifest.json").read_text())
    assert set(manifest) == {"schema_version", "schema_source", "paths", "terms"}
    schema_version = (root / "src/schema_org/schema_version.py").read_text()
    assert "SCHEMA_VERSION = '30.0'" in schema_version
    assert "SCHEMA_SOURCE" not in schema_version
    assert "SHA256" not in schema_version

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
