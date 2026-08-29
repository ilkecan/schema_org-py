from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS
from .model import ClassDefinition, EnumerationMember, PropertyDefinition, Subject, schema_name, schema_uri
from .naming import constant_name, enum_member_name, module_name, property_name

SCHEMA_HTTP = "http://schema.org/"
SCHEMA_HTTPS = "https://schema.org/"


class ValidationError(ValueError):
    pass


class Vocabulary:
    TOP_LEVEL_RESERVED_NAMES = frozenset({
        "SchemaModel", "SchemaEnum", "CircularReferenceError", "JsonValue",
        "SchemaScalar", "SchemaValue", "PropertyMetadata", "ClassMetadata",
        "EnumerationMemberMetadata", "SCHEMA_VERSION", "SCHEMA_TYPE",
        "SCHEMA_TYPES", "SCHEMA_PROPERTIES", "model_config", "model_fields",
    })

    def __init__(self, subjects: Iterable[Subject], *, naming=None):
        self.naming = naming
        self.subjects = tuple(subjects)
        self._by_uri: dict[str, Subject] = {}
        by_name: dict[str, list[Subject]] = {}
        for subject in self.subjects:
            if subject.uri in self._by_uri:
                raise ValidationError(f"Duplicate schema URI {subject.uri}")
            if subject.type_is("Class") and subject.type_is("Property"):
                raise ValidationError(f"Schema subject {subject.uri} is both a class and property")
            self._by_uri[subject.uri] = subject
            by_name.setdefault(subject.name, []).append(subject)
        logical_collisions = [
            f"{name} ({', '.join(sorted(subject.uri for subject in subjects))})"
            for name, subjects in sorted(by_name.items())
            if len(subjects) > 1
        ]
        if logical_collisions:
            raise ValidationError(f"Duplicate schema name {'; '.join(logical_collisions)}")
        self.classes = tuple(sorted((s for s in self.subjects if s.type_is("Class")), key=lambda s: s.name))
        self.properties = tuple(sorted((s for s in self.subjects if s.type_is("Property")), key=lambda s: s.name))
        self._class_by_name = {s.name: s for s in self.classes}
        self._property_by_name = {s.name: s for s in self.properties}
        self.enumeration_classes = tuple(s for s in self.classes if self.descendant(s.name, "Enumeration"))
        self.datatype_classes = tuple(s for s in self.classes if self.descendant(s.name, "DataType"))
        class_names = set(self._class_by_name)
        self.enumeration_members = tuple(sorted(
            (EnumerationMember(
                s.name,
                s.uri,
                tuple(sorted(name for name in s.type if name in class_names)),
                s.label,
                s.comment,
            ) for s in self.subjects
             if not s.type_is("Class") and not s.type_is("Property")
             and any(name in self._class_by_name and self.descendant(name, "Enumeration") for name in s.type)),
            key=lambda member: member.name,
        ))
        self._validate_references()
        self._validate_graph()
        self._validate_names()

    @classmethod
    def from_graph(cls, graph: Graph) -> "Vocabulary":
        subjects: list[Subject] = []
        uris = sorted({str(item) for item in graph.subjects() if _is_schema_uri(item)})
        for uri in uris:
            subject = URIRef(uri)

            def objects(*predicates: URIRef) -> tuple[object, ...]:
                return tuple(sorted(
                    (item for predicate in predicates for item in graph.objects(subject, predicate)),
                    key=str,
                ))

            def uri_terms(name: str, *predicates: URIRef) -> tuple[str, ...]:
                values = objects(*predicates)
                if any(not isinstance(value, URIRef) for value in values):
                    raise ValidationError(f"Schema subject {uri} has non-URI {name} value")
                return tuple(_term(value) for value in values)

            types = uri_terms("rdf:type", RDF.type)
            if not types:
                raise ValidationError(f"Schema subject {uri} has no rdf:type")
            type_set = set(types)
            if "Class" in type_set and "Property" in type_set:
                raise ValidationError(f"Schema subject {uri} is both a class and property")
            labels = objects(RDFS.label)
            if any(not isinstance(value, Literal) for value in labels):
                raise ValidationError(f"Schema subject {uri} has non-literal rdfs:label value")
            if not labels:
                raise ValidationError(f"Schema subject {uri} has no rdfs:label")
            if len(labels) > 1:
                raise ValidationError(f"Schema subject {uri} has multiple rdfs:label values")
            comments = objects(RDFS.comment)
            if any(not isinstance(value, Literal) for value in comments):
                raise ValidationError(f"Schema subject {uri} has non-literal rdfs:comment value")
            if len(comments) > 1:
                raise ValidationError(f"Schema subject {uri} has multiple rdfs:comment values")
            inverse_values = uri_terms("inverseOf", *_schema_values("inverseOf"))
            superseded_values = uri_terms("supersededBy", *_schema_values("supersededBy"))
            if len(inverse_values) > 1:
                raise ValidationError(f"Schema subject {uri} has multiple inverseOf values")
            if len(superseded_values) > 1:
                raise ValidationError(f"Schema subject {uri} has multiple supersededBy values")
            subjects.append(Subject(
                uri=uri,
                types=types,
                parents=uri_terms("subClassOf", RDFS.subClassOf, *_schema_values("subClassOf")),
                domains=uri_terms("domainIncludes", *_schema_values("domainIncludes")),
                ranges=uri_terms("rangeIncludes", *_schema_values("rangeIncludes")),
                inverse_of=inverse_values[0] if inverse_values else None,
                superseded_by=superseded_values[0] if superseded_values else None,
                equivalent_class=uri_terms("equivalentClass", OWL.equivalentClass),
                equivalent_properties=uri_terms("equivalentProperty", OWL.equivalentProperty),
                same_as=uri_terms("sameAs", OWL.sameAs, *_schema_values("sameAs")),
                subproperty_of=uri_terms("subPropertyOf", RDFS.subPropertyOf, *_schema_values("subPropertyOf")),
                label=str(labels[0]),
                comment=str(comments[0]) if comments else "",
                contributors=uri_terms("contributor", *_schema_values("contributor")),
                sources=uri_terms("source", *_schema_values("source")),
            ))
        return cls(subjects)

    @classmethod
    def from_file(cls, path: str | Path) -> "Vocabulary":
        graph = Graph()
        try:
            graph.parse(str(path), format="turtle")
        except Exception as error:
            raise ValidationError(f"Schema could not be parsed: {error}") from error
        return cls.from_graph(graph)

    def canonical_records(self) -> tuple[tuple[object, ...], ...]:
        return tuple(sorted((
            (
                subject.uri, subject.types, subject.parents, subject.domains, subject.ranges,
                subject.inverse_of, subject.superseded_by, subject.equivalent_class,
                subject.equivalent_properties, subject.same_as, subject.subproperty_of,
                subject.label, subject.comment, subject.contributors, subject.sources,
            )
            for subject in self.subjects
        ), key=lambda record: str(record[0])))


    @property
    def ordinary_classes(self) -> tuple[Subject, ...]:
        excluded = set(self.datatype_classes) | set(self.enumeration_classes)
        return tuple(s for s in self.classes if s not in excluded)

    def direct_parents(self, subject_or_name: Subject | str) -> tuple[str, ...]:
        subject = self._subject(subject_or_name)
        values = (*subject.parents, *subject.types)
        return tuple(sorted({
            name for value in values
            if (name := schema_name(value)) in self._class_by_name
            and name not in {"Class", "Property"}
        }))

    def external_parents(self, subject_or_name: Subject | str) -> tuple[str, ...]:
        subject = self._subject(subject_or_name)
        return tuple(sorted({
            _external_term(value) for value in subject.parents
            if not schema_name(value) or schema_name(value) in {"Class", "Property"}
        }))

    def ancestry(self, subject_or_name: Subject | str) -> tuple[str, ...]:
        queue = deque(self.direct_parents(subject_or_name))
        result: list[str] = []
        seen: set[str] = set()
        while queue:
            current = queue.popleft()
            if current in seen:
                continue
            seen.add(current)
            result.append(current)
            queue.extend(self.direct_parents(current))
        return tuple(result)

    def descendants(self, name: str) -> tuple[str, ...]:
        return tuple(sorted(s.name for s in self.classes if name in self.ancestry(s.name)))

    def direct_properties(self, type_name: str) -> tuple[Subject, ...]:
        return tuple(sorted((p for p in self.properties if type_name in self.property_domains(p)), key=lambda p: p.name))

    def property_domains(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({
            name for value in subject.domains
            if (name := schema_name(value)) in self._class_by_name
            and name not in {"Class", "Property"}
        }))

    def property_external_domains(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({
            _external_term(value) for value in subject.domains
            if not schema_name(value) or schema_name(value) in {"Class", "Property"}
        }))

    def property_ranges(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({
            name for value in subject.ranges
            if (name := schema_name(value)) in self._class_by_name
            and name not in {"Class", "Property"}
        }))

    def property_external_ranges(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({
            _external_term(value) for value in subject.ranges
            if not schema_name(value) or schema_name(value) in {"Class", "Property"}
        }))

    def data_type(self, name: str) -> bool:
        return any(s.name == name for s in self.datatype_classes)

    def enumeration(self, name: str) -> bool:
        return any(s.name == name for s in self.enumeration_classes)

    def descendant_of(self, name: str, ancestor: str) -> bool:
        return self.descendant(name, ancestor)

    def class_definition(self, name: str) -> ClassDefinition:
        subject = self._subject(name)
        supersedes = next((candidate.name for candidate in self.classes if candidate.superseded_by == subject.uri), None)
        return ClassDefinition(
            name=subject.name, uri=subject.uri, parents=self.direct_parents(subject),
            external_parents=self.external_parents(subject),
            equivalent_classes=subject.equivalent_class,
            superseded_by=schema_name(subject.superseded_by) if subject.superseded_by else None,
            supersedes=supersedes, label=subject.label, comment=subject.comment,
            contributors=subject.contributors, sources=subject.sources,
            properties=tuple(p.name for p in self.direct_properties(subject.name)),
            is_datatype=self.data_type(subject.name), is_enumeration=self.enumeration(subject.name),
        )

    def property_definition(self, name: str) -> PropertyDefinition:
        subject = self._property(name)
        supersedes = next((candidate.name for candidate in self.properties if candidate.superseded_by == subject.uri), None)
        return PropertyDefinition(
            name=subject.name, uri=subject.uri, domains=self.property_domains(subject),
            external_domains=self.property_external_domains(subject), ranges=self.property_ranges(subject),
            external_ranges=self.property_external_ranges(subject),
            inverse_of=schema_name(subject.inverse_of) if subject.inverse_of else None,
            superseded_by=schema_name(subject.superseded_by) if subject.superseded_by else None,
            supersedes=supersedes,
            equivalent_properties=tuple(schema_name(value) or value for value in subject.equivalent_properties),
            subproperty_of=tuple(schema_name(value) or value for value in subject.subproperty_of),
            label=subject.label, comment=subject.comment,
            contributors=subject.contributors, sources=subject.sources,
        )

    def descendant(self, name: str, ancestor: str, seen: set[str] | None = None) -> bool:
        if name == ancestor:
            return True
        seen = set() if seen is None else seen
        if name in seen or name not in self._class_by_name:
            return False
        seen.add(name)
        return any(self.descendant(parent, ancestor, seen) for parent in self.direct_parents(name))

    def _subject(self, subject_or_name: Subject | str) -> Subject:
        return subject_or_name if isinstance(subject_or_name, Subject) else self._class_by_name[str(subject_or_name)]

    def _property(self, property_: Subject | str) -> Subject:
        return property_ if isinstance(property_, Subject) else self._property_by_name[str(property_)]

    def _validate_references(self) -> None:
        errors: list[str] = []

        def validate(
            subject: Subject,
            relation: str,
            values: Iterable[str | None],
            expected: dict[str, Subject],
        ) -> None:
            for value in values:
                if value is None:
                    continue
                name = schema_name(value)
                if name in {"Class", "Property"}:
                    continue
                if name and name not in expected:
                    errors.append(
                        f"Unknown schema.org {relation} {name} for {subject.name}"
                    )

        for subject in self.classes:
            validate(subject, "parent", subject.parents, self._class_by_name)
            validate(
                subject,
                "equivalent class",
                subject.equivalent_class,
                self._class_by_name,
            )
            validate(
                subject,
                "superseding class",
                (subject.superseded_by,),
                self._class_by_name,
            )
        for property_ in self.properties:
            validate(property_, "domain", property_.domains, self._class_by_name)
            validate(property_, "range", property_.ranges, self._class_by_name)
            validate(
                property_,
                "inverse property",
                (property_.inverse_of,),
                self._property_by_name,
            )
            validate(
                property_,
                "superseding property",
                (property_.superseded_by,),
                self._property_by_name,
            )
            validate(
                property_,
                "equivalent property",
                property_.equivalent_properties,
                self._property_by_name,
            )
            validate(
                property_,
                "superproperty",
                property_.subproperty_of,
                self._property_by_name,
            )
        for subject in self.subjects:
            if subject.type_is("Class") or subject.type_is("Property"):
                continue
            validate(
                subject,
                "type",
                (
                    value
                    for value in subject.types
                    if (schema_name(value) or value) not in {"Class", "Property"}
                ),
                self._class_by_name,
            )
        if errors:
            raise ValidationError("; ".join(errors))

    def _validate_graph(self) -> None:
        colors: dict[str, int] = {}

        def visit(name: str, path: list[str]) -> None:
            color = colors.get(name, 0)
            if color == 1:
                cycle = (path[path.index(name):] if name in path else path) + [name]
                raise ValidationError(f"Inheritance cycle involving {', '.join(dict.fromkeys(cycle))}")
            if color == 2:
                return
            colors[name] = 1
            for parent in self.direct_parents(name):
                visit(parent, path + [name])
            colors[name] = 2

        for subject in self.classes:
            visit(subject.name, [])

    def _validate_names(self) -> None:
        class_names = [s.name for s in self.classes]
        self._validate_name_set(class_names, constant_name, "class", self.TOP_LEVEL_RESERVED_NAMES)
        self._validate_name_set(class_names, module_name, "module")
        ordinary_names = [s.name for s in self.ordinary_classes]
        self._validate_name_set(
            [*ordinary_names, *(s.name for s in self.enumeration_classes)],
            constant_name,
            "root export",
            self.TOP_LEVEL_RESERVED_NAMES,
        )
        property_reserved = {
            "schema_id", "schema_type", "model_config", "model_fields",
            "model_dump", "model_validate", "to_jsonld", "to_jsonld_json",
        }
        self._validate_name_set((p.name for p in self.properties), property_name, "property", property_reserved)
        for enum in self.enumeration_classes:
            members = [m.name for m in self.enumeration_members if any(self.descendant(type_name, enum.name) for type_name in m.types)]
            self._validate_name_set(
                members, enum_member_name, f"enumeration {enum.name}",
                frozenset({"SCHEMA_NAME", "SCHEMA_TYPES", "ABSTRACT_TYPE", "VALUES"}),
            )

    @staticmethod
    def _validate_name_set(names: Iterable[str], mapper, kind: str, reserved=frozenset()) -> None:
        groups: dict[str, list[str]] = {}
        for name in names:
            try:
                mapped = mapper(name)
            except (TypeError, ValueError) as error:
                raise ValidationError(f"Invalid Python {kind} name for {name}: {error}") from error
            groups.setdefault(mapped, []).append(name)
        collisions = [
            f"{', '.join(values)} ({mapped})"
            for mapped, values in sorted(groups.items())
            if len(values) > 1 or mapped in reserved
        ]
        if collisions:
            raise ValidationError(f"Python {kind} collision for {'; '.join(collisions)}")


def _is_schema_uri(value: object) -> bool:
    text = str(value)
    return text.startswith(SCHEMA_HTTP) or text.startswith(SCHEMA_HTTPS)


def _term(value: object) -> str:
    text = str(value)
    if text == str(RDFS.Class):
        return "Class"
    if text == str(RDF.Property):
        return "Property"
    return text


def _external_term(value: str) -> str:
    name = schema_name(value)
    return name if name in {"Class", "Property"} else value


def _schema(name: str) -> URIRef:
    return URIRef(f"{SCHEMA_HTTPS}{name}")


def _schema_values(name: str) -> tuple[URIRef, URIRef]:
    return URIRef(f"{SCHEMA_HTTP}{name}"), URIRef(f"{SCHEMA_HTTPS}{name}")


def _first_term(values: tuple[object, ...]) -> str | None:
    return _term(values[0]) if values else None
