from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS

from .model import ClassDefinition, EnumerationMember, PropertyDefinition, Subject, schema_name, schema_uri
from .naming import constant_name, enum_member_name, property_name, snake_name

SCHEMA_HTTP = "http://schema.org/"
SCHEMA_HTTPS = "https://schema.org/"


class ValidationError(ValueError):
    pass


class Vocabulary:
    TOP_LEVEL_RESERVED_NAMES = frozenset({
        "SchemaModel", "SchemaEnum", "CircularReferenceError", "JsonValue",
        "SCHEMA_VERSION", "SCHEMA_TYPE", "SCHEMA_TYPES", "SCHEMA_PROPERTIES",
    })

    def __init__(self, subjects: Iterable[Subject], *, naming=None):
        self.naming = naming
        self.subjects = tuple(subjects)
        self._by_uri: dict[str, Subject] = {}
        for subject in self.subjects:
            if subject.uri in self._by_uri:
                raise ValidationError(f"Duplicate schema URI {subject.uri}")
            self._by_uri[subject.uri] = subject
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
            values = lambda *predicates: tuple(
                sorted(
                    {item for predicate in predicates for item in graph.objects(subject, predicate)},
                    key=str,
                )
            )
            types = tuple(_term(value) for value in values(RDF.type))
            parents = tuple(_term(value) for value in values(RDFS.subClassOf, *_schema_values("subClassOf")))
            domains = tuple(_term(value) for value in values(*_schema_values("domainIncludes")))
            ranges = tuple(_term(value) for value in values(*_schema_values("rangeIncludes")))
            inverse_values = values(*_schema_values("inverseOf"))
            superseded_values = values(*_schema_values("supersededBy"))
            equivalent_class = tuple(_term(value) for value in values(OWL.equivalentClass))
            equivalent_property_values = values(OWL.equivalentProperty)
            same_as_values = values(OWL.sameAs, *_schema_values("sameAs"))
            subproperty_values = values(RDFS.subPropertyOf, *_schema_values("subPropertyOf"))
            labels = tuple(str(value) for value in values(RDFS.label))
            comments = tuple(str(value) for value in values(RDFS.comment))
            contributors = tuple(_term(value) for value in values(*_schema_values("contributor")))
            sources = tuple(_term(value) for value in values(*_schema_values("source")))
            if not types:
                raise ValidationError(f"Schema subject {uri} has no rdf:type")
            type_set = set(types)
            if "Class" in type_set and "Property" in type_set:
                raise ValidationError(f"Schema subject {uri} is both a class and property")
            if type_set & {"Class", "Property"} and not labels:
                raise ValidationError(f"Schema subject {uri} has no rdfs:label")
            if len(labels) > 1:
                raise ValidationError(f"Schema subject {uri} has multiple rdfs:label values")
            if len(comments) > 1:
                raise ValidationError(f"Schema subject {uri} has multiple rdfs:comment values")
            subjects.append(Subject(
                uri=uri, types=types, parents=parents, domains=domains, ranges=ranges,
                inverse_of=_first_term(inverse_values), superseded_by=_first_term(superseded_values),
                equivalent_class=equivalent_class,
                equivalent_properties=tuple(_term(value) for value in equivalent_property_values),
                same_as=tuple(_term(value) for value in same_as_values),
                subproperty_of=tuple(_term(value) for value in subproperty_values),
                label=labels[0] if labels else "", comment=comments[0] if comments else "",
                contributors=contributors, sources=sources,
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

    def term_name(self, value: str | Subject) -> str:
        return value.name if isinstance(value, Subject) else schema_name(value) or str(value)

    def schema_name(self, value: str) -> str | None:
        return schema_name(value)

    def schema_uri(self, name: str) -> str:
        return schema_uri(name)

    def schema_uri_p(self, value: str) -> bool:
        return _is_schema_uri(value)

    def direct_parents(self, subject_or_name: Subject | str) -> tuple[str, ...]:
        subject = self._subject(subject_or_name)
        values = (*subject.parents, *subject.types)
        return tuple(sorted({name for value in values if (name := schema_name(value)) in self._class_by_name and name not in {"Class", "Property"}}))
    def external_parents(self, subject_or_name: Subject | str) -> tuple[str, ...]:
        subject = self._subject(subject_or_name)
        return tuple(sorted({value for value in subject.parents if not schema_name(value)}))

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
        return tuple(sorted({schema_name(value) for value in subject.domains if schema_name(value) in self._class_by_name}))

    def property_external_domains(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({value for value in subject.domains if not schema_name(value)}))

    def property_ranges(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({schema_name(value) for value in subject.ranges if schema_name(value) in self._class_by_name}))

    def property_external_ranges(self, property_: Subject | str) -> tuple[str, ...]:
        subject = self._property(property_)
        return tuple(sorted({value for value in subject.ranges if not schema_name(value)}))

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
        for subject in self.classes:
            for parent in subject.parents:
                name = schema_name(parent)
                if name and name not in self._class_by_name:
                    errors.append(f"Unknown schema.org parent {name} for {subject.name}")
        for property_ in self.properties:
            for value in property_.domains:
                name = schema_name(value)
                if name and name not in self._class_by_name:
                    errors.append(f"Unknown schema.org domain {name} for {property_.name}")
            for value in property_.ranges:
                name = schema_name(value)
                if name and name not in self._class_by_name:
                    errors.append(f"Unknown schema.org range {name} for {property_.name}")
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
        self._validate_name_set((s.name for s in self.classes), constant_name, "class", self.TOP_LEVEL_RESERVED_NAMES)
        self._validate_name_set((s.name for s in self.classes), snake_name, "file")
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
            groups.setdefault(mapper(name), []).append(name)
        collisions = [f"{', '.join(values)} ({mapped})" for mapped, values in sorted(groups.items()) if len(values) > 1 or mapped in reserved]
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


def _schema(name: str) -> URIRef:
    return URIRef(f"{SCHEMA_HTTPS}{name}")


def _schema_values(name: str) -> tuple[URIRef, URIRef]:
    return URIRef(f"{SCHEMA_HTTP}{name}"), URIRef(f"{SCHEMA_HTTPS}{name}")


def _first_term(values: tuple[object, ...]) -> str | None:
    return _term(values[0]) if values else None
