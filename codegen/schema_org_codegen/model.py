from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Subject:
    uri: str
    types: tuple[str, ...]
    parents: tuple[str, ...]
    domains: tuple[str, ...]
    ranges: tuple[str, ...]
    inverse_of: str | None = None
    superseded_by: str | None = None
    equivalent_class: tuple[str, ...] = ()
    equivalent_properties: tuple[str, ...] = ()
    same_as: tuple[str, ...] = ()
    subproperty_of: tuple[str, ...] = ()
    label: str = ""
    comment: str = ""
    contributors: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()

    @property
    def name(self) -> str:
        return schema_name(self.uri) or self.uri

    @property
    def type(self) -> tuple[str, ...]:
        return tuple(schema_name(value) or value for value in self.types)

    def type_is(self, marker: str) -> bool:
        return marker in self.type


@dataclass(frozen=True, slots=True)
class ClassDefinition:
    name: str
    uri: str
    parents: tuple[str, ...]
    external_parents: tuple[str, ...]
    equivalent_classes: tuple[str, ...]
    superseded_by: str | None
    supersedes: str | None
    label: str
    comment: str
    contributors: tuple[str, ...]
    sources: tuple[str, ...]
    properties: tuple[str, ...]
    is_datatype: bool = False
    is_enumeration: bool = False


@dataclass(frozen=True, slots=True)
class PropertyDefinition:
    name: str
    uri: str
    domains: tuple[str, ...]
    external_domains: tuple[str, ...]
    ranges: tuple[str, ...]
    external_ranges: tuple[str, ...]
    inverse_of: str | None
    superseded_by: str | None
    supersedes: str | None
    equivalent_properties: tuple[str, ...]
    subproperty_of: tuple[str, ...]
    label: str
    comment: str
    contributors: tuple[str, ...]
    sources: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class EnumerationMember:
    name: str
    uri: str
    types: tuple[str, ...]
    label: str
    comment: str


def schema_name(value: Any) -> str | None:
    text = str(value)
    for prefix in ("https://schema.org/", "http://schema.org/"):
        if text.startswith(prefix):
            return text[len(prefix):]
    return None


def schema_uri(name: str) -> str:
    return f"https://schema.org/{name}"
