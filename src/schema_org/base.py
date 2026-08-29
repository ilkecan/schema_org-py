from __future__ import annotations

from collections.abc import Mapping
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
    supersedes: tuple[str, ...] = ()
    equivalent_properties: tuple[str, ...] = ()
    subproperty_of: tuple[str, ...] = ()
    domains: tuple[str, ...] = ()
    external_domains: tuple[str, ...] = ()
    comment: str = ""
    label: str = ""
    contributors: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ClassMetadata:
    name: str
    uri: str
    parents: tuple[str, ...] = ()
    external_parents: tuple[str, ...] = ()
    equivalent_classes: tuple[str, ...] = ()
    superseded_by: str | None = None
    supersedes: tuple[str, ...] = ()
    label: str = ""
    comment: str = ""
    contributors: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()
    properties: tuple[str, ...] = ()
    is_datatype: bool = False
    is_enumeration: bool = False


@dataclass(frozen=True, slots=True)
class EnumerationMemberMetadata:
    name: str
    uri: str
    types: tuple[str, ...] = ()
    label: str = ""
    comment: str = ""


class SchemaModel(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True, populate_by_name=True)

    SCHEMA_TYPE: ClassVar[str]
    SCHEMA_TYPES: ClassVar[tuple[str, ...]]
    SCHEMA_PROPERTIES: ClassVar[tuple[PropertyMetadata, ...]] = ()

    @model_validator(mode="before")
    @classmethod
    def _validate_schema_values(cls, data: object) -> object:
        if isinstance(data, dict):
            active = {id(data)}
            metadata = {item.schema_name: item for item in cls.SCHEMA_PROPERTIES}
            for key, value in data.items():
                field = cls.model_fields.get(key) or next(
                    (candidate for candidate in cls.model_fields.values() if candidate.alias == key),
                    None,
                )
                alias = field.alias if field is not None else key
                property_metadata = metadata.get(alias)
                if property_metadata is not None and _has_generated_range(property_metadata.ranges):
                    _walk_typed_input(
                        value,
                        path=f"$.{alias}",
                        active=active,
                        expected_models=_generated_range_names(property_metadata.ranges),
                    )
                else:
                    if property_metadata is not None and "Number" in property_metadata.ranges:
                        _reject_number_bool(value, path=f"$.{alias}")
                    _walk_schema_value(value, path=f"$.{alias}", active=active)
            return data
        _walk_schema_value(data, path="$", active=set())
        return data
    @classmethod
    def model_rebuild(
        cls,
        *,
        force: bool = False,
        raise_errors: bool = True,
        _parent_namespace_depth: int = 2,
        _types_namespace: Mapping[str, object] | None = None,
    ) -> bool | None:
        if _types_namespace is None and cls.__module__.startswith("schema_org.models."):
            from schema_org import registry
            registry.rebuild(cls.SCHEMA_TYPE)
            return True
        return super().model_rebuild(
            force=force,
            raise_errors=raise_errors,
            _parent_namespace_depth=_parent_namespace_depth,
            _types_namespace=_types_namespace,
        )

    def __setattr__(self, name: str, value: object) -> None:
        if name in type(self).model_fields and _contains_identity(value, self):
            substitute = self.model_copy(deep=False)
            candidate = _replace_identity(value, self, substitute, {})
            super().__setattr__(name, candidate)
            validated = self.__dict__[name]
            self.__dict__[name] = _replace_identity(validated, substitute, self, {})
            return
        super().__setattr__(name, value)

    def to_jsonld(self) -> dict[str, JsonValue]:
        return _serialize(self, root=True, active={"objects": set()}, path="$" )  # type: ignore[return-value]

    def to_jsonld_json(self, *, indent: int | None = None) -> str:
        return json.dumps(self.to_jsonld(), indent=indent, ensure_ascii=False, separators=None if indent is not None else (",", ":"))


SchemaScalar: TypeAlias = str | int | float | bool | SchemaModel | SchemaEnum
SchemaMap = TypeAliasType("SchemaMap", dict[str, "SchemaScalar | SchemaMap"])
SchemaValue = TypeAliasType("SchemaValue", SchemaScalar | SchemaMap | list[SchemaScalar | SchemaMap])


def _generated_model(value: SchemaModel) -> bool:
    try:
        from schema_org import registry
        return registry.get_model(value.SCHEMA_TYPE) is type(value)
    except (AttributeError, KeyError, TypeError):
        return False


def _reject_number_bool(value: object, *, path: str) -> None:
    if type(value) is bool:
        raise ValueError(f"invalid Number value at {path}")
    if isinstance(value, list):
        for index, item in enumerate(value):
            _reject_number_bool(item, path=f"{path}[{index}]")


def _generated_enum(value: SchemaEnum) -> bool:
    try:
        from schema_org import registry
        enum_name = type(value).__name__
        enum = registry.ENUM_BY_SCHEMA.get(enum_name)
        return enum is type(value)
    except (AttributeError, KeyError, TypeError):
        return False
def _generated_range_names(ranges: tuple[str, ...]) -> tuple[str, ...]:
    try:
        from schema_org import registry
        return tuple(name for name in ranges if name in registry._MODEL_CLASSES)
    except (AttributeError, ImportError):
        return ()


def _has_generated_range(ranges: tuple[str, ...]) -> bool:
    return bool(_generated_range_names(ranges))

def _typed_field(expected_models: tuple[str, ...], key: str):
    try:
        from schema_org import registry
        for name in expected_models:
            model = registry.get_model(name)
            field = model.model_fields.get(key) or next(
                (candidate for candidate in model.model_fields.values() if candidate.alias == key),
                None,
            )
            if field is not None:
                return model, field
    except (AttributeError, KeyError, TypeError):
        pass
    return None, None

def _walk_typed_input(
    value: object,
    *,
    path: str,
    active: set[int],
    expected_models: tuple[str, ...] = (),
) -> None:
    if value is None or type(value) in {str, bool, int, float, date, datetime, time}:
        return
    if isinstance(value, SchemaModel):
        if not _generated_model(value):
            raise ValueError("schema values must be generated Schema.org models")
        object_id = id(value)
        if object_id in active:
            raise CircularReferenceError(f"Circular reference at {path}")
        active.add(object_id)
        try:
            metadata = {item.schema_name: item for item in type(value).SCHEMA_PROPERTIES}
            for field_name, field in type(value).model_fields.items():
                if field_name in {"schema_id", "schema_type"}:
                    continue
                item = getattr(value, field_name)
                if item is not None:
                    alias = field.alias or field_name
                    property_metadata = metadata.get(alias)
                    ranges = property_metadata.ranges if property_metadata is not None else ()
                    _walk_typed_input(
                        item,
                        path=f"{path}.{alias}",
                        active=active,
                        expected_models=_generated_range_names(ranges),
                    )
        finally:
            active.remove(object_id)
        return
    if isinstance(value, SchemaEnum):
        if not _generated_enum(value):
            raise ValueError("schema values must be generated Schema.org enum members")
        return
    if isinstance(value, list):
        object_id = id(value)
        if object_id in active:
            raise CircularReferenceError(f"Circular reference at {path}")
        active.add(object_id)
        try:
            for index, item in enumerate(value):
                _walk_typed_input(
                    item,
                    path=f"{path}[{index}]",
                    active=active,
                    expected_models=expected_models,
                )
        finally:
            active.remove(object_id)
        return
    if isinstance(value, dict):
        object_id = id(value)
        if object_id in active:
            raise CircularReferenceError(f"Circular reference at {path}")
        active.add(object_id)
        try:
            for key, item in value.items():
                if not isinstance(key, str):
                    raise ValueError(f"invalid {path}: mapping keys must be str")
                model, field = _typed_field(expected_models, key)
                if field is None:
                    next_path = f"{path}[{key!r}]"
                    next_models = expected_models
                else:
                    alias = field.alias or key
                    next_path = f"{path}.{alias}"
                    property_metadata = next(
                        (
                            candidate
                            for candidate in model.SCHEMA_PROPERTIES
                            if candidate.schema_name == alias
                        ),
                        None,
                    )
                    ranges = property_metadata.ranges if property_metadata is not None else ()
                    next_models = _generated_range_names(ranges)
                _walk_typed_input(
                    item,
                    path=next_path,
                    active=active,
                    expected_models=next_models,
                )
        finally:
            active.remove(object_id)
        return

def _walk_schema_value(
    value: object,
    *,
    path: str,
    active: set[int],
    allow_list: bool = True,
) -> None:
    if value is None:
        return
    if isinstance(value, SchemaModel):
        if not _generated_model(value):
            raise ValueError("schema values must be generated Schema.org models")
        object_id = id(value)
        if object_id in active:
            raise CircularReferenceError(f"Circular reference at {path}")
        active.add(object_id)
        try:
            metadata = {item.schema_name: item for item in type(value).SCHEMA_PROPERTIES}
            for field_name, field in type(value).model_fields.items():
                if field_name in {"schema_id", "schema_type"}:
                    continue
                item = getattr(value, field_name)
                if item is not None:
                    alias = field.alias or field_name
                    property_metadata = metadata.get(alias)
                    _walk_schema_value(
                        item,
                        path=f"{path}.{alias}",
                        active=active,
                    )
        finally:
            active.remove(object_id)
        return
    if isinstance(value, SchemaEnum):
        if not _generated_enum(value):
            raise ValueError("schema values must be generated Schema.org enum members")
        return
    if type(value) in {str, bool, int, float}:
        return
    if type(value) in {date, datetime, time}:
        return
    if isinstance(value, (str, bool, int, float, date, datetime, time)):
        raise ValueError(f"invalid schema value at {path}")
    if isinstance(value, list):
        if not allow_list:
            raise ValueError(f"invalid schema value at {path}: nested lists are not allowed")
        object_id = id(value)
        if object_id in active:
            raise CircularReferenceError(f"Circular reference at {path}")
        active.add(object_id)
        try:
            for index, item in enumerate(value):
                _walk_schema_value(
                    item,
                    path=f"{path}[{index}]",
                    active=active,
                    allow_list=False,
                )
        finally:
            active.remove(object_id)
        return
    if isinstance(value, dict):
        object_id = id(value)
        if object_id in active:
            raise CircularReferenceError(f"Circular reference at {path}")
        active.add(object_id)
        try:
            for key, item in value.items():
                if not isinstance(key, str):
                    raise ValueError(f"invalid {path}: mapping keys must be str")
                _walk_schema_value(
                    item,
                    path=f"{path}[{key!r}]",
                    active=active,
                    allow_list=False,
                )
        finally:
            active.remove(object_id)
        return
    raise ValueError(f"invalid schema value at {path}")


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
    if isinstance(value, (list, dict)):
        active.add(object_id)
        try:
            values = value if isinstance(value, list) else value.values()
            return any(_contains_identity(item, target, active) for item in values)
        finally:
            active.remove(object_id)
    return False


def _replace_identity(value: object, target: object, replacement: object, seen: dict[int, object]) -> object:
    if value is target:
        return replacement
    if not isinstance(value, (list, dict)):
        return value
    object_id = id(value)
    if object_id in seen:
        return seen[object_id]
    if isinstance(value, list):
        result: list[object] = []
        seen[object_id] = result
        result.extend(_replace_identity(item, target, replacement, seen) for item in value)
        return result
    result_dict: dict[object, object] = {}
    seen[object_id] = result_dict
    for key, item in value.items():
        result_dict[key] = _replace_identity(item, target, replacement, seen)
    return result_dict


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
