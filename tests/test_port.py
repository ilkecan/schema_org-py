from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest
from pydantic import ValidationError
from schema_org_codegen import Subject, Vocabulary
from schema_org_codegen import ValidationError as CodegenValidationError
from schema_org_codegen.naming import constant_name, module_name, property_name
from schema_org_codegen.schema_version import SchemaVersion

from schema_org import (
    CircularReferenceError,
    ItemAvailability,
    Offer,
    Person,
    PostalAddress,
)

ROOT = Path(__file__).parents[1]


def subject(name, types=("Class",), parents=(), domains=(), ranges=()):
    return Subject(
        uri=f"https://schema.org/{name}", types=tuple(types), parents=tuple(parents),
        domains=tuple(domains), ranges=tuple(ranges), label=name, comment="",
    )


def test_v30_vocabulary_and_naming():
    vocabulary = Vocabulary.from_file(ROOT / "codegen/data/schema.ttl")
    assert len(vocabulary.classes) == 937
    assert vocabulary.ancestry("Quantity") == ("DataType",)
    assert vocabulary.ancestry("SequentialArt")[:2] == ("Book", "VisualArtwork")
    assert constant_name("3DModel") == "ThreeDModel"
    assert module_name("3DModel") == "three_d_model"
    assert property_name("jobTitle") == "job_title"


def test_vocabulary_rejects_dangling_and_cycles():
    with pytest.raises(CodegenValidationError, match="Missing"):
        Vocabulary([subject("Thing"), subject("Child", parents=("https://schema.org/Missing",))])
    with pytest.raises(CodegenValidationError, match=r"A.*B"):
        Vocabulary([subject("A", parents=("https://schema.org/B",)), subject("B", parents=("https://schema.org/A",))])


def test_schema_version_headers_are_strict(tmp_path):
    valid = "# schema_org_release: v30.0\n# schema_org_source: https://schema.org/version/30.0/schemaorg-all-https.ttl\n"
    path = tmp_path / "schema-version-fixture.ttl"
    path.write_text(valid, encoding="utf-8")
    assert SchemaVersion.current(path).version == "30.0"
    path.write_text(valid + "# schema_org_source: https://schema.org/version/30.0/schemaorg-all-https.ttl\n", encoding="utf-8")
    with pytest.raises(CodegenValidationError):
        SchemaVersion.current(path)


def test_strict_models_aliases_enums_and_assignment():
    person = Person(name="Ada", address=PostalAddress(address_locality="London"), birth_date=date(1990, 1, 2))
    output = person.to_jsonld()
    assert output["@context"] == "https://schema.org"
    assert output["address"]["addressLocality"] == "London"
    assert output["birthDate"] == "1990-01-02"
    assert Offer(availability=ItemAvailability.IN_STOCK).to_jsonld()["availability"] == "https://schema.org/InStock"
    with pytest.raises(ValidationError):
        Person(name=1)
    with pytest.raises(ValidationError):
        Person(unknown_field="x")
    person.name = "Grace"
    with pytest.raises(ValidationError):
        person.name = 1


def test_cycles_are_rejected_before_serialization():
    person = Person(name="Ada")
    with pytest.raises(ValidationError):
        person.colleague = [person]
    object.__setattr__(person, "colleague", [person])
    with pytest.raises(CircularReferenceError, match=r"\$\.colleague\[0\]"):
        person.to_jsonld()


def test_range_less_values_reject_nested_arrays_and_bad_keys():
    from schema_org import Observation

    for value in ([1, [2]], {1: "bad"}, date.today()):
        with pytest.raises(ValidationError):
            Observation(measured_property=value)


def test_parser_preserves_http_predicates_and_rejects_bad_shapes(tmp_path):
    from schema_org_codegen import Vocabulary

    valid = _fixture_schema(
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix old: <http://schema.org/> .\n"
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
        "schema:Child a rdfs:Class ; rdfs:label \"Child\" ; old:subClassOf schema:Thing .\n"
        "schema:value a rdf:Property ; rdfs:label \"value\" ; old:domainIncludes schema:Child ; old:rangeIncludes schema:Text .\n"
        "schema:Text a rdfs:Class ; rdfs:label \"Text\" .\n"
    )
    path = tmp_path / "valid.ttl"
    path.write_text(valid, encoding="utf-8")
    vocabulary = Vocabulary.from_file(path)
    assert vocabulary.direct_parents("Child") == ("Thing",)
    assert vocabulary.property_ranges("value") == ("Text",)

    malformed = tmp_path / "malformed.ttl"
    malformed.write_text(_fixture_schema(
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class .\n"
    ), encoding="utf-8")
    with pytest.raises(CodegenValidationError, match="no rdfs:label"):
        Vocabulary.from_file(malformed)


def test_v30_runtime_identity_and_multiple_inheritance():
    from schema_org import Book, Credential, Error, SequentialArt, VisualArtwork
    from schema_org.schema_version import SCHEMA_VERSION

    assert SCHEMA_VERSION == "30.0"
    assert Credential.SCHEMA_TYPE == "Credential"
    assert Error.SCHEMA_TYPE == "Error"
    from schema_org import registry
    assert registry.DATATYPES["Quantity"][0] == "DataType"
    assert SequentialArt.SCHEMA_TYPES[1:3] == ("Book", "VisualArtwork")
    assert issubclass(SequentialArt, Book)
    assert issubclass(SequentialArt, VisualArtwork)
    assert "book_format" in SequentialArt.model_fields
    assert "art_edition" in SequentialArt.model_fields


def test_json_serialization_and_exact_declared_dates():
    from datetime import datetime

    with pytest.raises(ValidationError):
        Person(birth_date=datetime(1990, 1, 2))
    encoded = Person(name="Ada").to_jsonld_json()
    assert '"@context":"https://schema.org"' in encoded



def test_non_generated_model_subclasses_are_rejected():
    from schema_org import Observation

    Person(name="Ada")

    class CustomPerson(Person):
        pass

    custom = CustomPerson.model_construct(name="Ada")
    with pytest.raises(ValidationError):
        Observation(measured_property=custom)

def _fixture_schema(statements: str) -> str:
    return (
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        + statements
    )


def test_reordered_equivalent_ttl_generates_identical_artifacts(tmp_path):
    from schema_org_codegen.generator import generate

    first_root = tmp_path / "first"
    second_root = tmp_path / "second"
    for root, statements in (
        (first_root, "@prefix schema: <https://schema.org/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\nschema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\nschema:Child a rdfs:Class ; rdfs:label \"Child\" ; rdfs:subClassOf schema:Thing .\n"),
        (second_root, "@prefix schema: <https://schema.org/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\nschema:Child rdfs:subClassOf schema:Thing ; rdfs:label \"Child\" ; a rdfs:Class .\nschema:Thing rdfs:label \"Thing\" ; a rdfs:Class .\n"),
    ):
        schema = root / "codegen/data/schema.ttl"
        schema.parent.mkdir(parents=True)
        schema.write_text(_fixture_schema(statements), encoding="utf-8")
        generate(schema, project_root=root, output_root=root)
    first_files = {
        path.relative_to(first_root).as_posix(): path.read_bytes()
        for path in (first_root / "src/schema_org").rglob("*") if path.is_file()
    }
    second_files = {
        path.relative_to(second_root).as_posix(): path.read_bytes()
        for path in (second_root / "src/schema_org").rglob("*") if path.is_file()
    }
    assert first_files == second_files
    assert json.loads((first_root / "codegen/generated_manifest.json").read_text()) == json.loads(
        (second_root / "codegen/generated_manifest.json").read_text()
    )


def test_generation_prunes_only_manifest_owned_stale_files(tmp_path):
    from schema_org_codegen.generator import generate

    root = tmp_path
    schema = root / "codegen/data/schema.ttl"
    schema.parent.mkdir(parents=True)
    schema.write_text(_fixture_schema(
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
        "schema:Child a rdfs:Class ; rdfs:label \"Child\" ; rdfs:subClassOf schema:Thing .\n"
    ), encoding="utf-8")
    generate(schema, project_root=root, output_root=root)
    stale = root / "src/schema_org/models/child.py"
    assert stale.exists()
    (root / "src/schema_org/handwritten.py").write_text("keep", encoding="utf-8")
    schema.write_text(_fixture_schema(
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
    ), encoding="utf-8")
    generate(schema, project_root=root, output_root=root)
    assert not stale.exists()
    assert (root / "src/schema_org/handwritten.py").read_text() == "keep"
