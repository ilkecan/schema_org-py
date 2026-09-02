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

@pytest.mark.parametrize(
    ("kind", "subject_kwargs"),
    [
        ("parent", {"parents": ("https://schema.org/Missing",)}),
        ("equivalent class", {"equivalent_class": ("https://schema.org/Missing",)}),
        ("superseding class", {"superseded_by": "https://schema.org/Missing"}),
    ],
)
def test_vocabulary_rejects_dangling_class_references(kind, subject_kwargs):
    with pytest.raises(ValidationError, match=kind):
        Vocabulary([subject("Thing"), subject("Child", **subject_kwargs)])


@pytest.mark.parametrize(
    ("kind", "subject_kwargs"),
    [
        ("domain", {"domains": ("https://schema.org/Missing",)}),
        ("range", {"ranges": ("https://schema.org/Missing",)}),
        ("inverse property", {"inverse_of": "https://schema.org/Missing"}),
        ("superseding property", {"superseded_by": "https://schema.org/Missing"}),
        ("equivalent property", {"equivalent_properties": ("https://schema.org/Missing",)}),
        ("superproperty", {"subproperty_of": ("https://schema.org/Missing",)}),
    ],
)
def test_vocabulary_rejects_dangling_property_references(kind, subject_kwargs):
    with pytest.raises(ValidationError, match=kind):
        Vocabulary([subject("Thing"), subject("value", ("Property",), **subject_kwargs)])

def test_vocabulary_rejects_dangling_enumeration_member_type():
    with pytest.raises(ValidationError, match="type"):
        Vocabulary([
            subject("Thing"),
            subject("Enumeration", parents=("https://schema.org/Thing",)),
            subject("Member", ("https://schema.org/Missing",)),
        ])


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


def test_vocabulary_rejects_emitted_namespace_name_collisions():
    with pytest.raises(ValidationError, match="root export"):
        Vocabulary([subject("Thing"), subject("SchemaMap")])
    with pytest.raises(ValidationError, match="class import"):
        Vocabulary([subject("Thing"), subject("Field", parents=("https://schema.org/Thing",))])
    with pytest.raises(ValidationError, match="property"):
        Vocabulary([
            subject("Thing"),
            subject("modelCopy", ("Property",), domains=("https://schema.org/Thing",)),
        ])


def test_vocabulary_rejects_leading_underscore_emitted_names():
    with pytest.raises(ValidationError, match="property"):
        Vocabulary([
            subject("Thing"),
            subject("_value", ("Property",), domains=("https://schema.org/Thing",)),
        ])
    with pytest.raises(ValidationError, match="enum member"):
        Vocabulary([
            subject("Thing"),
            subject("Enumeration", parents=("https://schema.org/Thing",)),
            subject("Status", parents=("https://schema.org/Enumeration",)),
            Subject(
                uri="https://schema.org/_Unknown",
                types=("https://schema.org/Status",),
                parents=(),
                domains=(),
                ranges=(),
                label="_Unknown",
                comment="",
            ),
        ])


def test_datatype_module_name_overlap_does_not_collide():
    Vocabulary([
        subject("Thing"),
        subject("DataType", parents=("https://schema.org/Thing",)),
        subject("FooBar", parents=("https://schema.org/Thing",)),
        subject("Foo_Bar", parents=("https://schema.org/DataType",)),
    ])


def test_vocabulary_from_graph_enforces_single_same_as(tmp_path: Path):
    path = tmp_path / "schema.ttl"
    path.write_text(
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" ; "
        "schema:sameAs <https://example.test/one>, <https://example.test/two> .\n",
        encoding="utf-8",
    )
    with pytest.raises(ValidationError, match="multiple sameAs"):
        Vocabulary.from_file(path)


@pytest.mark.parametrize(
    "statement",
    [
        "rdf:type \"Class\"",
        "rdfs:subClassOf \"Thing\"",
        "schema:domainIncludes \"Thing\"",
        "schema:rangeIncludes \"Thing\"",
        "schema:inverseOf \"value\"",
        "schema:supersededBy \"value\"",
        "owl:equivalentClass \"Thing\"",
        "owl:equivalentProperty \"value\"",
        "owl:sameAs \"value\"",
        "rdfs:subPropertyOf \"value\"",
        "schema:contributor \"person\"",
        "schema:source \"source\"",
    ],
)
def test_vocabulary_from_graph_rejects_non_uri_values_in_uri_relations(
    tmp_path: Path, statement: str
):
    path = tmp_path / "schema.ttl"
    path.write_text(
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
        "schema:value a rdf:Property ; rdfs:label \"value\" ; "
        + statement
        + " .\n",
        encoding="utf-8",
    )
    with pytest.raises(ValidationError, match="non-URI"):
        Vocabulary.from_file(path)


@pytest.mark.parametrize(
    "statement",
    [
        "schema:Thing rdfs:label \"Thing\"",
        "schema:Thing a rdfs:Class",
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\", \"Other\"",
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" ; rdfs:comment \"one\", \"two\"",
    ],
)
def test_vocabulary_from_graph_rejects_missing_or_ambiguous_metadata(
    tmp_path: Path, statement: str
):
    path = tmp_path / "schema.ttl"
    path.write_text(
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        + statement
        + " .\n",
        encoding="utf-8",
    )
    with pytest.raises(ValidationError):
        Vocabulary.from_file(path)


@pytest.mark.parametrize("predicate", ["schema:inverseOf", "schema:supersededBy"])
def test_vocabulary_from_graph_rejects_multiple_singleton_relations(
    tmp_path: Path, predicate: str
):
    path = tmp_path / "schema.ttl"
    path.write_text(
        "# schema_org_release: v1.0\n"
        "# schema_org_source: https://schema.org/version/1.0/schemaorg-all-https.ttl\n"
        "@prefix schema: <https://schema.org/> .\n"
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "schema:Thing a rdfs:Class ; rdfs:label \"Thing\" .\n"
        "schema:value a rdf:Property ; rdfs:label \"value\" ; "
        + predicate
        + " schema:Thing, schema:Thing2 .\n"
        "schema:Thing2 a rdfs:Class ; rdfs:label \"Thing2\" .\n",
        encoding="utf-8",
    )
    with pytest.raises(ValidationError, match="multiple"):
        Vocabulary.from_file(path)


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("https://schema.org/Thing", "http://schema.org/Thing"),
        ("http://schema.org/Thing", "https://schema.org/Thing"),
    ],
)
def test_vocabulary_rejects_both_http_https_logical_collisions(first: str, second: str):
    with pytest.raises(ValidationError, match="Duplicate schema name"):
        Vocabulary([
            Subject(
                uri=first,
                types=("Class",),
                parents=(),
                domains=(),
                ranges=(),
                label="Thing",
                comment="",
            ),
            Subject(
                uri=second,
                types=("Class",),
                parents=(),
                domains=(),
                ranges=(),
                label="Thing",
                comment="",
            ),
        ])


def test_vocabulary_rejects_class_and_module_collisions():
    with pytest.raises(ValidationError, match="Python class collision"):
        Vocabulary([subject("Thing"), subject("3DModel"), subject("ThreeDModel")])
    with pytest.raises(ValidationError, match="Python module collision"):
        Vocabulary([
            subject("Thing"),
            subject("FooBar"),
            subject("Foo_Bar"),
        ])


def test_vocabulary_rejects_duplicate_exact_uris():
    duplicate = subject("Thing")
    with pytest.raises(ValidationError, match="Duplicate schema URI"):
        Vocabulary([duplicate, duplicate])
