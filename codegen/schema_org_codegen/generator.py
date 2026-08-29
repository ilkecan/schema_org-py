from __future__ import annotations

import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
from typing import Iterable

from .naming import constant_name, enum_member_name, module_name, property_name
from .parser import parse
from .schema_version import SchemaVersion
from .manifest import read_manifest, validate_manifest
from .transaction import apply_transaction
ROOT = Path(__file__).resolve().parents[2]
PRIMITIVE_ALIASES = {
    "Text": "str", "URL": "str", "Boolean": "bool", "Integer": "int",
    "Float": "float", "Number": "int | float", "Date": "date",
    "DateTime": "datetime", "Time": "time",
}


def generate(
    schema_file: str | Path = ROOT / "codegen/data/schema.ttl",
    *,
    project_root: str | Path = ROOT,
    output_root: str | Path | None = None,
) -> dict[str, object]:
    project_root = Path(project_root)
    output_root = Path(output_root) if output_root is not None else project_root
    schema_file = Path(schema_file)
    version = SchemaVersion.current(schema_file)
    vocabulary = parse(schema_file)
    _preflight_mro(vocabulary)
    with tempfile.TemporaryDirectory(prefix="schema-org-generated-", dir=project_root) as temporary:
        staged_package = Path(temporary) / "src/schema_org"
        staged_package.mkdir(parents=True)
        _render_package(vocabulary, version, staged_package)
        staged_manifest = Path(temporary) / "generated_manifest.json"
        manifest = _manifest(vocabulary, version, staged_package)
        staged_manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        _commit_tree(staged_package, output_root / "src/schema_org", staged_manifest, manifest)
    return manifest


def _render_package(vocabulary: Vocabulary, version: SchemaVersion, package: Path) -> None:
    models = sorted(vocabulary.ordinary_classes, key=lambda subject: subject.name)
    for subject in models:
        _atomic_write(package / "models" / f"{module_name(subject.name)}.py", _generated(_render_model(vocabulary, subject.name)))
    _atomic_write(package / "models" / "__init__.py", _generated(_render_models_init(models)))
    _atomic_write(package / "enums.py", _generated(_render_enums(vocabulary)))
    _atomic_write(package / "datatypes.py", _generated(_render_datatypes(vocabulary)))
    _atomic_write(package / "registry.py", _generated(_render_registry(vocabulary, version)))
    _atomic_write(package / "schema_version.py", _generated(_render_schema_version(version)))
    _atomic_write(package / "__init__.py", _generated(_render_root_init(vocabulary)))
    _atomic_write(package / "py.typed", "")


def _generated(content: str) -> str:
    return (
        "# Generated Python code is licensed under MIT.\n"
        "# Schema.org descriptions are licensed under CC BY-SA 3.0.\n"
        "# See LICENSE-SCHEMA-ORG.txt.\n\n"
        + content
    )
def _render_model(vocabulary: Vocabulary, name: str) -> str:
    subject = next(s for s in vocabulary.ordinary_classes if s.name == name)
    parents = _ordered_direct_parents(vocabulary, name)
    bases = ", ".join(constant_name(parent) for parent in parents) or "SchemaModel"
    effective = _effective_properties(vocabulary, name)
    lines = [
        "from __future__ import annotations",
        "",
        "from typing import ClassVar, Literal",
        "",
        "from schema_org.base import PropertyMetadata, SchemaModel, SchemaValue",
        "from pydantic import Field",
    ]
    imports = _model_imports(vocabulary, effective, parents, name)
    lines.extend(imports)
    lines.extend(["", f"class {constant_name(name)}({bases}):"])
    lines.append(f"    __doc__ = {_class_description(vocabulary, name)!r}")
    lines.extend([
        f"    SCHEMA_TYPE: ClassVar[str] = {name!r}",
        f"    SCHEMA_TYPES: ClassVar[tuple[str, ...]] = {(name, *vocabulary.ancestry(name))!r}",
        "    SCHEMA_PROPERTIES: ClassVar[tuple[PropertyMetadata, ...]] = (",
    ])
    for property_name_ in effective:
        definition = vocabulary.property_definition(property_name_)
        lines.append(
            "        PropertyMetadata(name=%r, schema_name=%r, schema_url=%r, ranges=%r, external_ranges=%r, "
            "inverse_of=%r, superseded_by=%r, supersedes=%r, equivalent_properties=%r, subproperty_of=%r, "
            "domains=%r, external_domains=%r, comment=%r, label=%r, contributors=%r, sources=%r)," % (
                property_name(property_name_), definition.name, definition.uri, definition.ranges,
                definition.external_ranges, definition.inverse_of, definition.superseded_by, definition.supersedes,
                definition.equivalent_properties, definition.subproperty_of, definition.domains,
                definition.external_domains, definition.comment, definition.label, definition.contributors, definition.sources,
            )
        )
    lines.append("    )")
    lines.append("    schema_id: str | None = Field(default=None, alias='@id')")
    lines.append(f"    schema_type: Literal[{name!r}] = Field(default={name!r}, alias='@type', frozen=True)")
    for property_name_ in sorted(vocabulary.direct_properties(name), key=lambda item: item.name):
        definition = vocabulary.property_definition(property_name_.name)
        annotation = _annotation(vocabulary, definition)
        description = _description(definition.comment, definition.superseded_by, definition.supersedes, definition.inverse_of)
        field_description = f", description={description!r}" if description else ""
        lines.append(f"    {property_name(definition.name)}: {annotation} = Field(default=None, alias={definition.name!r}{field_description})")
    lines.append("")
    return "\n".join(lines)


def _description(comment: str, superseded_by: str | None, supersedes: str | None, inverse_of: str | None) -> str:
    parts = [comment] if comment else []
    if supersedes:
        parts.append(f"Supersedes `{supersedes}`.")
    if superseded_by:
        parts.append(f"Superseded by `{superseded_by}`.")
    if inverse_of:
        parts.append(f"Inverse-property: `{inverse_of}`.")
    return "\n\n".join(parts)


def _class_description(vocabulary: Vocabulary, name: str) -> str:
    definition = vocabulary.class_definition(name)
    return _description(
        f"{definition.uri}\n\n{definition.comment}" if definition.comment else definition.uri,
        definition.superseded_by,
        definition.supersedes,
        None,
    )


def _ordered_direct_parents(vocabulary: Vocabulary, name: str) -> tuple[str, ...]:
    ordinary = {subject.name for subject in vocabulary.ordinary_classes}
    remaining = set(vocabulary.direct_parents(name)) & ordinary
    ordered: list[str] = []
    while remaining:
        available = sorted(
            candidate for candidate in remaining
            if not any(candidate != other and vocabulary.descendant(other, candidate) for other in remaining)
        )
        if not available:
            raise ValidationError(f"Unable to order direct parents for {name}: {sorted(remaining)!r}")
        selected = available[0]
        ordered.append(selected)
        remaining.remove(selected)
    return tuple(ordered)


def _preflight_mro(vocabulary: Vocabulary) -> None:
    cache: dict[str, tuple[str, ...]] = {}

    def linearize(name: str) -> tuple[str, ...]:
        if name in cache:
            return cache[name]
        parents = _ordered_direct_parents(vocabulary, name)
        sequences = [list(linearize(parent)) for parent in parents]
        sequences.append(list(parents))
        result = [name]
        while any(sequences):
            candidate = next(
                (sequence[0] for sequence in sequences if sequence and all(sequence[0] not in other[1:] for other in sequences)),
                None,
            )
            if candidate is None:
                raise ValidationError(f"Invalid C3 MRO for {name} with direct parents {list(parents)!r}")
            result.append(candidate)
            sequences = [sequence[1:] if sequence and sequence[0] == candidate else sequence for sequence in sequences]
        cache[name] = tuple(result)
        return cache[name]

    for subject in vocabulary.ordinary_classes:
        linearize(subject.name)

def _model_imports(vocabulary: Vocabulary, properties: Iterable[str], parents: Iterable[str], current_name: str) -> list[str]:
    imports: set[str] = set()
    ordinary = {subject.name for subject in vocabulary.ordinary_classes}
    for parent in parents:
        imports.add(f"from schema_org.models.{module_name(parent)} import {constant_name(parent)}")
    for property_name_ in properties:
        definition = vocabulary.property_definition(property_name_)
        for range_name in definition.ranges:
            if range_name == current_name:
                continue
            if range_name in ordinary:
                continue
            if vocabulary.enumeration(range_name):
                imports.add(f"from schema_org.enums import {constant_name(range_name)}")
            elif vocabulary.data_type(range_name):
                imports.add(f"from schema_org.datatypes import {constant_name(range_name)}")
    return sorted(imports)


def _annotation(vocabulary: Vocabulary, definition) -> str:
    names: list[str] = []
    ordinary = {subject.name for subject in vocabulary.ordinary_classes}
    for range_name in definition.ranges:
        if range_name == "Property":
            continue
        if range_name in ordinary or vocabulary.enumeration(range_name) or vocabulary.data_type(range_name):
            names.append(constant_name(range_name))
    names = list(dict.fromkeys(names))
    if not names:
        return "SchemaValue | None"
    item = " | ".join(names)
    return f"{item} | list[{item}] | None"


def _effective_properties(vocabulary: Vocabulary, name: str) -> tuple[str, ...]:
    names = {property_.name for property_ in vocabulary.direct_properties(name)}
    names.update(property_.name for ancestor in vocabulary.ancestry(name) for property_ in vocabulary.direct_properties(ancestor))
    return tuple(sorted(names))


def _render_models_init(models) -> str:
    lines = [
        "from importlib import import_module",
        "from typing import TYPE_CHECKING",
        "",
        "if TYPE_CHECKING:",
    ]
    lines.extend(f"    from .{module_name(subject.name)} import {constant_name(subject.name)}" for subject in models)
    lines.extend([
        "",
        "_MODEL_MODULES = {",
    ])
    lines.extend(f"    {constant_name(subject.name)!r}: {module_name(subject.name)!r}," for subject in models)
    lines.extend([
        "}",
        "",
        "def __getattr__(name: str):",
        "    module_name = _MODEL_MODULES.get(name)",
        "    if module_name is None:",
        "        raise AttributeError(name)",
        "    return getattr(import_module(f'.{module_name}', __name__), name)",
        "",
        "def __dir__():",
        "    return sorted(set(globals()) | set(_MODEL_MODULES))",
    ])
    return "\n".join(lines) + "\n"


def _render_enums(vocabulary: Vocabulary) -> str:
    lines = ["from __future__ import annotations", "", "from schema_org.base import SchemaEnum", ""]
    for enum in vocabulary.enumeration_classes:
        lines.append(f"class {constant_name(enum.name)}(SchemaEnum):")
        members = [member for member in vocabulary.enumeration_members if any(vocabulary.descendant(type_name, enum.name) for type_name in member.types)]
        members = sorted({member.name: member for member in members}.values(), key=lambda member: member.name)
        if not members:
            lines.append("    pass")
        else:
            for member in members:
                lines.append(f"    {enum_member_name(member.name)} = {member.uri.replace('http://schema.org/', 'https://schema.org/')!r}")
        lines.append("")
    return "\n".join(lines)


def _datatype_alias(vocabulary: Vocabulary, name: str) -> str:
    if name in PRIMITIVE_ALIASES:
        return PRIMITIVE_ALIASES[name]
    ancestry = (name, *vocabulary.ancestry(name))
    for candidate in ("Integer", "Float", "Number", "Boolean", "DateTime", "Date", "Time", "Text", "URL"):
        if candidate in ancestry:
            return PRIMITIVE_ALIASES[candidate]
    return "str"


def _render_datatypes(vocabulary: Vocabulary) -> str:
    lines = ["from __future__ import annotations", "", "from datetime import date, datetime, time", "", ""]
    for datatype in vocabulary.datatype_classes:
        lines.append(f"{constant_name(datatype.name)} = {_datatype_alias(vocabulary, datatype.name)}")
    return "\n".join(lines) + "\n"


def _render_registry(vocabulary: Vocabulary, version: SchemaVersion) -> str:
    ordinary = sorted(vocabulary.ordinary_classes, key=lambda subject: subject.name)
    ordinary_names = {subject.name for subject in ordinary}
    lines = [
        "from __future__ import annotations",
        "",
        "from importlib import import_module",
        "from collections.abc import Iterator, Mapping",
        "from types import MappingProxyType",
        "from schema_org.base import ClassMetadata, EnumerationMemberMetadata, PropertyMetadata",
    ]
    lines.append("_MODEL_MODULES = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {module_name(s.name)!r}," for s in ordinary)
    lines.append("})")
    lines.append("_MODEL_CLASSES = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {constant_name(s.name)!r}," for s in ordinary)
    lines.append("})")
    lines.append("_ENUM_NAMES = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {constant_name(s.name)!r}," for s in vocabulary.enumeration_classes)
    lines.append("})")
    lines.append("MODULE_BY_SCHEMA = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {'schema_org.models.' + module_name(s.name)!r}," for s in ordinary)
    lines.append("})")
    lines.append("PARENTS = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {vocabulary.direct_parents(s.name)!r}," for s in sorted(vocabulary.classes, key=lambda item: item.name))
    lines.append("})")
    lines.append("CLASS_METADATA = MappingProxyType({")
    for subject in sorted(vocabulary.classes, key=lambda item: item.name):
        definition = vocabulary.class_definition(subject.name)
        lines.append(
            f"    {definition.name!r}: ClassMetadata(name={definition.name!r}, uri={definition.uri!r}, "
            f"parents={definition.parents!r}, external_parents={definition.external_parents!r}, "
            f"equivalent_classes={definition.equivalent_classes!r}, superseded_by={definition.superseded_by!r}, "
            f"supersedes={definition.supersedes!r}, label={definition.label!r}, comment={definition.comment!r}, "
            f"contributors={definition.contributors!r}, sources={definition.sources!r}, properties={definition.properties!r}, "
            f"is_datatype={definition.is_datatype!r}, is_enumeration={definition.is_enumeration!r}),"
        )
    lines.append("})")
    lines.append("PROPERTY_BY_SCHEMA = MappingProxyType({")
    for property_ in vocabulary.properties:
        definition = vocabulary.property_definition(property_.name)
        lines.append(
            f"    {definition.name!r}: PropertyMetadata(name={property_name(definition.name)!r}, "
            f"schema_name={definition.name!r}, schema_url={definition.uri!r}, ranges={definition.ranges!r}, "
            f"external_ranges={definition.external_ranges!r}, inverse_of={definition.inverse_of!r}, "
            f"superseded_by={definition.superseded_by!r}, supersedes={definition.supersedes!r}, "
            f"equivalent_properties={definition.equivalent_properties!r}, subproperty_of={definition.subproperty_of!r}, "
            f"domains={definition.domains!r}, external_domains={definition.external_domains!r}, "
            f"comment={definition.comment!r}, label={definition.label!r}, contributors={definition.contributors!r}, sources={definition.sources!r}),"
        )
    lines.append("})")
    lines.append("ENUM_MEMBER_METADATA = MappingProxyType({")
    for member in vocabulary.enumeration_members:
        lines.append(
            f"    {member.name!r}: EnumerationMemberMetadata(name={member.name!r}, uri={member.uri!r}, "
            f"types={member.types!r}, label={member.label!r}, comment={member.comment!r}),"
        )
    lines.append("})")
    lines.append("ENUM_DIRECT_MEMBERS = MappingProxyType({")
    for enum in vocabulary.enumeration_classes:
        members = tuple(sorted(
            member.name for member in vocabulary.enumeration_members
            if enum.name in member.types
        ))
        lines.append(f"    {enum.name!r}: {members!r},")
    lines.append("})")
    lines.append("ENUM_PARENTS = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {vocabulary.direct_parents(s.name)!r}," for s in vocabulary.enumeration_classes)
    lines.append("})")
    lines.append("ENUM_MEMBERS = MappingProxyType({")
    for enum in vocabulary.enumeration_classes:
        members = tuple(sorted(
            member.name for member in vocabulary.enumeration_members
            if any(vocabulary.descendant(type_name, enum.name) for type_name in member.types)
        ))
        lines.append(f"    {enum.name!r}: {members!r},")
    lines.append("})")
    lines.append("DATATYPES = MappingProxyType({")
    lines.extend(f"    {s.name!r}: {vocabulary.ancestry(s.name)!r}," for s in vocabulary.datatype_classes)
    lines.append("})")
    lines.append("_DEPENDENCIES = MappingProxyType({")
    for subject in ordinary:
        dependencies = set(vocabulary.direct_parents(subject.name)) & ordinary_names
        dependencies.update(range_name for property_name_ in _effective_properties(vocabulary, subject.name) for range_name in vocabulary.property_definition(property_name_).ranges if range_name in ordinary_names)
        lines.append(f"    {subject.name!r}: {tuple(sorted(dependencies))!r},")
    lines.append("})")
    lines.extend([
        f"SCHEMA_VERSION = {version.version!r}",
        "",
        "class _LazyModels(Mapping[str, type]):",
        "    def __getitem__(self, name: str) -> type:",
        "        return get_model(name)",
        "    def __iter__(self) -> Iterator[str]:",
        "        return iter(_MODEL_MODULES)",
        "    def __len__(self) -> int:",
        "        return len(_MODEL_MODULES)",
        "",
        "MODEL_BY_SCHEMA = _LazyModels()",
        "",
        "def get_model(name: str) -> type:",
        "    module = import_module(f\"schema_org.models.{_MODEL_MODULES[name]}\")",
        "    model = getattr(module, _MODEL_CLASSES[name])",
        "    rebuild(name)",
        "    return model",
        "",
        "def ancestry(name: str) -> tuple[str, ...]:",
        "    result = []",
        "    queue = list(PARENTS.get(name, ()))",
        "    seen = set()",
        "    while queue:",
        "        current = queue.pop(0)",
        "        if current in seen:",
        "            continue",
        "        seen.add(current)",
        "        result.append(current)",
        "        queue.extend(PARENTS.get(current, ()))",
        "    return tuple(result)",
        "",
        "def rebuild(name: str) -> type:",
        "    loaded = {}",
        "    def load(current: str):",
        "        if current in loaded:",
        "            return",
        "        module = import_module(f\"schema_org.models.{_MODEL_MODULES[current]}\")",
        "        loaded[current] = getattr(module, _MODEL_CLASSES[current])",
        "        for dependency in _DEPENDENCIES[current]:",
        "            load(dependency)",
        "    load(name)",
        "    import schema_org.datatypes as datatypes",
        "    import schema_org.enums as enums",
        "    namespace = {**loaded, **vars(datatypes), **vars(enums)}",
        "    loaded[name].model_rebuild(force=True, _types_namespace=namespace)",
        "    return loaded[name]",
        
        "",
        "class _LazyEnums(Mapping[str, type]):",
        "    def __getitem__(self, name: str) -> type:",
        "        return getattr(import_module('schema_org.enums'), _ENUM_NAMES[name])",
        "    def __iter__(self) -> Iterator[str]:",
        "        return iter(_ENUM_NAMES)",
        "    def __len__(self) -> int:",
        "        return len(_ENUM_NAMES)",
        "",
        "ENUM_BY_SCHEMA = _LazyEnums()",
    ])
    return "\n".join(lines) + "\n"


def _render_schema_version(version: SchemaVersion) -> str:
    return f"SCHEMA_VERSION = {version.version!r}\n"


def _render_root_init(vocabulary: Vocabulary) -> str:
    ordinary = sorted(vocabulary.ordinary_classes, key=lambda item: item.name)
    lines = [
        "from importlib import import_module",
        "from typing import TYPE_CHECKING",
        "",
        "from .base import CircularReferenceError, ClassMetadata, EnumerationMemberMetadata, JsonValue, PropertyMetadata, SchemaEnum, SchemaMap, SchemaModel, SchemaScalar, SchemaValue",
        "from .schema_version import SCHEMA_VERSION",
        "",
        "if TYPE_CHECKING:",
    ]
    lines.extend(f"    from .models.{module_name(s.name)} import {constant_name(s.name)}" for s in ordinary)
    lines.extend([
        "",
        "_MODEL_MODULES = {",
    ])
    lines.extend(f"    {constant_name(s.name)!r}: {module_name(s.name)!r}," for s in ordinary)
    lines.extend([
        "}",
        "_ENUM_NAMES = {",
    ])
    lines.extend(f"    {constant_name(s.name)!r}: {constant_name(s.name)!r}," for s in vocabulary.enumeration_classes)
    lines.extend([
        "}",
        "",
        "def __getattr__(name: str):",
        "    module_name = _MODEL_MODULES.get(name)",
        "    if module_name is not None:",
        "        model = getattr(import_module(f'.models.{module_name}', __name__), name)",
        "        from . import registry",
        "        return registry.rebuild(next(term for term, cls_name in registry._MODEL_CLASSES.items() if cls_name == name))",
        "    enum_name = _ENUM_NAMES.get(name)",
        "    if enum_name is not None:",
        "        return getattr(import_module('.enums', __name__), enum_name)",
        "    raise AttributeError(name)",
        "",
        "__all__ = [",
    ])
    lines.extend(f"    {constant_name(s.name)!r}," for s in ordinary)
    lines.extend(f"    {constant_name(s.name)!r}," for s in vocabulary.enumeration_classes)
    lines.extend([
        "    'SCHEMA_VERSION',", "    'ClassMetadata',", "    'EnumerationMemberMetadata',",
        "    'SchemaMap',", "    'SchemaModel',", "    'SchemaEnum',",
        "    'CircularReferenceError',",
        "]",
    ])
    return "\n".join(lines) + "\n"


def _manifest(vocabulary: Vocabulary, version: SchemaVersion, package: Path) -> dict[str, object]:
    paths = sorted(f"src/schema_org/{path.relative_to(package).as_posix()}" for path in package.rglob("*") if path.is_file())
    terms = {
        "classes": sorted(s.name for s in vocabulary.classes),
        "datatypes": sorted(s.name for s in vocabulary.datatype_classes),
        "enumerations": sorted(s.name for s in vocabulary.enumeration_classes),
        "enumeration_members": sorted(m.name for m in vocabulary.enumeration_members),
        "properties": sorted(s.name for s in vocabulary.properties),
    }
    return {
        "schema_version": version.version,
        "schema_source": version.schema_source,
        "paths": paths,
        "terms": terms,
    }

def _commit_tree(staged: Path, destination: Path, staged_manifest: Path, manifest: dict[str, object]) -> None:
    root = destination.parent.parent
    previous_manifest_path = root / "codegen/generated_manifest.json"
    previous = read_manifest(previous_manifest_path, project_root=root) if previous_manifest_path.exists() else None
    validated = validate_manifest(manifest)
    previous_paths = set(previous["paths"]) if previous is not None else set()
    new_paths = set(validated["paths"])
    replacements = {
        relative: (staged / Path(relative).relative_to("src/schema_org")).read_bytes()
        for relative in sorted(new_paths)
    }
    replacements["codegen/generated_manifest.json"] = staged_manifest.read_bytes()
    apply_transaction(root, replacements, previous_paths - new_paths)


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def _atomic_replace(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(source, destination)
