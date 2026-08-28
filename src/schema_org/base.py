from __future__ import annotations

from datetime import date, datetime, time
from dataclasses import dataclass
from enum import Enum
import json
from typing import ClassVar, TypeAlias
from typing_extensions import TypeAliasType

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

JsonValue: TypeAlias = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]


class CircularReferenceError(ValueError):
    pass


class SchemaEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True, slots=True)
class PropertyMetadata:
    name: str
    schema_name: str
    schema_url: str
    ranges: tuple[str, ...] = ()
    external_ranges: tuple[str, ...] = ()
    inverse_of: str | None = None
    superseded_by: str | None = None
    supersedes: str | None = None
    equivalent_properties: tuple[str, ...] = ()
    subproperty_of: tuple[str, ...] = ()
    domains: tuple[str, ...] = ()
    external_domains: tuple[str, ...] = ()
    comment: str = ""
    label: str = ""
    contributors: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()

class SchemaModel(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True, populate_by_name=True)

    SCHEMA_TYPE: ClassVar[str]
    SCHEMA_TYPES: ClassVar[tuple[str, ...]]
    SCHEMA_PROPERTIES: ClassVar[tuple[PropertyMetadata, ...]] = ()

    @model_validator(mode="before")
    @classmethod
    def _reject_non_generated_models(cls, data: object) -> object:
        def visit(value: object) -> None:
            if isinstance(value, SchemaModel):
                if not type(value).__module__.startswith("schema_org.models."):
                    raise ValueError("schema values must be generated Schema.org models")
                return
            if isinstance(value, list):
                for item in value:
                    visit(item)
            elif isinstance(value, dict):
                for item in value.values():
                    visit(item)

        visit(data)
        return data

    def __setattr__(self, name: str, value: object) -> None:
        try:
            super().__setattr__(name, value)
        except ValidationError:
            if name in type(self).model_fields and _contains_identity(value, self):
                self.__dict__[name] = value
                self.__pydantic_fields_set__.add(name)
                return
            raise

    def to_jsonld(self) -> dict[str, JsonValue]:
        return _serialize(self, root=True, active={"objects": set()}, path="$")  # type: ignore[return-value]

    def to_jsonld_json(self, *, indent: int | None = None) -> str:
        return json.dumps(self.to_jsonld(), indent=indent, ensure_ascii=False, separators=None if indent is not None else (",", ":"))


def _contains_identity(value: object, target: SchemaModel, active: set[int] | None = None) -> bool:
    if value is target:
        return True
    if isinstance(value, SchemaModel):
        return False
    if active is None:
        active = set()
    object_id = id(value)
    if object_id in active:
        return False
    if isinstance(value, list):
        active.add(object_id)
        try:
            return any(_contains_identity(item, target, active) for item in value)
        finally:
            active.remove(object_id)
    if isinstance(value, dict):
        active.add(object_id)
        try:
            return any(_contains_identity(item, target, active) for item in value.values())
        finally:
            active.remove(object_id)
    return False
 
SchemaScalar: TypeAlias = str | int | float | bool | SchemaModel | SchemaEnum
SchemaValue = TypeAliasType("SchemaValue", SchemaScalar | dict[str, "SchemaValue"] | list[SchemaScalar])


def _serialize(value: object, *, root: bool, active: dict[str, object], path: str) -> JsonValue:
    if isinstance(value, SchemaModel):
        object_id = id(value)
        objects: set[int] = active["objects"]  # type: ignore[assignment]
        if object_id in objects:
            raise CircularReferenceError(f"Circular reference at {path}")
        objects.add(object_id)
        try:
            result: dict[str, JsonValue] = {}
            if root:
                result["@context"] = "https://schema.org"
            result["@type"] = value.SCHEMA_TYPE
            if value.schema_id is not None:
                result["@id"] = value.schema_id
            for field_name, field in type(value).model_fields.items():
                if field_name in {"schema_id", "schema_type"}:
                    continue
                item = getattr(value, field_name)
                if item is None:
                    continue
                alias = field.alias or field_name
                result[alias] = _serialize(item, root=False, active=active, path=f"{path}.{alias}")
            return result
        finally:
            objects.remove(object_id)
    if isinstance(value, SchemaEnum):
        return value.value
    if isinstance(value, datetime | date | time):
        return value.isoformat()
    if isinstance(value, list):
        object_id = id(value)
        objects: set[int] = active["objects"]  # type: ignore[assignment]
        if object_id in objects:
            raise CircularReferenceError(f"Circular reference at {path}")
        objects.add(object_id)
        try:
            return [_serialize(item, root=False, active=active, path=f"{path}[{index}]") for index, item in enumerate(value)]
        finally:
            objects.remove(object_id)
    if isinstance(value, dict):
        object_id = id(value)
        objects: set[int] = active["objects"]  # type: ignore[assignment]
        if object_id in objects:
            raise CircularReferenceError(f"Circular reference at {path}")
        objects.add(object_id)
        try:
            result = {}
            for key, item in value.items():
                if not isinstance(key, str):
                    raise ValueError(f"invalid {path}: mapping keys must be str")
                result[key] = _serialize(item, root=False, active=active, path=f'{path}[{key!r}]')
            return result
        finally:
            objects.remove(object_id)
    return value  # type: ignore[return-value]
