from pathlib import Path

import pytest

from schema_org_codegen import Subject, ValidationError, Vocabulary


def subject(name, types=("Class",), **kwargs):
    return Subject(
        uri=f"https://schema.org/{name}",
        types=tuple(types),
        parents=tuple(kwargs.get("parents", ())),
        domains=tuple(kwargs.get("domains", ())),
        ranges=tuple(kwargs.get("ranges", ())),
        inverse_of=kwargs.get("inverse_of"),
        superseded_by=kwargs.get("superseded_by"),
        equivalent_class=tuple(kwargs.get("equivalent_class", ())),
        equivalent_properties=tuple(kwargs.get("equivalent_properties", ())),
        subproperty_of=tuple(kwargs.get("subproperty_of", ())),
        label=name,
        comment="",
    )


def test_vocabulary_rejects_wrong_internal_reference_kinds():
    with pytest.raises(ValidationError, match="domain"):
        Vocabulary([subject("Thing"), subject("value", ("Property",), domains=("https://schema.org/value",))])
    with pytest.raises(ValidationError, match="inverse property"):
        Vocabulary([subject("Thing"), subject("value", ("Property",), inverse_of="https://schema.org/Thing")])


def test_vocabulary_preserves_external_meta_ranges():
    vocabulary = Vocabulary([
        subject("Thing"),
        subject("value", ("Property",), domains=("https://schema.org/Thing",), ranges=("https://schema.org/Property", "https://example.test/Value")),
    ])
    assert vocabulary.property_ranges("value") == ()
    assert vocabulary.property_external_ranges("value") == ("Property", "https://example.test/Value")


def test_vocabulary_rejects_http_https_logical_collisions():
    with pytest.raises(ValidationError, match="Duplicate schema name"):
        Vocabulary([subject("Thing"), Subject(
            uri="http://schema.org/Thing", types=("Class",), parents=(), domains=(), ranges=(), label="Thing", comment="",
        )])


def test_vocabulary_from_graph_rejects_non_uri_relationship(tmp_path: Path):
    path = tmp_path / "schema.ttl"
    path.write_text(
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
        "schema:value a rdf:Property ; rdfs:label \"value\" ; schema:domainIncludes \"Thing\" .\n",
        encoding="utf-8",
    )
    with pytest.raises(ValidationError, match="non-URI domain"):
        Vocabulary.from_file(path)
