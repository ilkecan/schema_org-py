from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
from typing import Iterable

from .naming import constant_name, enum_member_name, module_name, property_name, snake_name
from .parser import parse
from .schema_version import SchemaVersion
from .vocabulary import Vocabulary

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
    canonical_hash = _canonical_hash(vocabulary)
    source_hash = version.source_sha256 or canonical_hash
    with tempfile.TemporaryDirectory(prefix="schema-org-generated-", dir=project_root) as temporary:
        staged_package = Path(temporary) / "src/schema_org"
        staged_package.mkdir(parents=True)
        _render_package(vocabulary, version, source_hash, canonical_hash, staged_package)
        staged_manifest = Path(temporary) / "generated_manifest.json"
        manifest = _manifest(vocabulary, version, source_hash, canonical_hash, staged_package)
        staged_manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        _commit_tree(staged_package, output_root / "src/schema_org")
        _atomic_replace(staged_manifest, output_root / "codegen/generated_manifest.json")
    return manifest


def _canonical_hash(vocabulary: Vocabulary) -> str:
    payload = json.dumps(vocabulary.canonical_records(), ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()



def _render_package(vocabulary: Vocabulary, version: SchemaVersion, source_hash: str, canonical_hash: str, package: Path) -> None:
    models = sorted(vocabulary.ordinary_classes, key=lambda subject: subject.name)
    for subject in models:
        _atomic_write(package / "models" / f"{module_name(subject.name)}.py", _generated(_render_model(vocabulary, subject.name)))
    _atomic_write(package / "models" / "__init__.py", _generated(_render_models_init(models)))
    _atomic_write(package / "enums.py", _generated(_render_enums(vocabulary)))
    _atomic_write(package / "datatypes.py", _generated(_render_datatypes(vocabulary)))
    _atomic_write(package / "registry.py", _generated(_render_registry(vocabulary, version)))
    _atomic_write(package / "schema_version.py", _generated(_render_schema_version(version, source_hash, canonical_hash)))
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
    direct_parents = [parent for parent in vocabulary.direct_parents(name) if parent in {s.name for s in vocabulary.ordinary_classes}]
    parents = [parent for parent in direct_parents if not any(parent != other and parent in vocabulary.ancestry(other) for other in direct_parents)]
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
    lines.append(f"    __doc__ = {subject.comment!r}" if subject.comment else "    pass")
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
        description = f", description={definition.comment!r}" if definition.comment else ""
        lines.append(f"    {property_name(definition.name)}: {annotation} = Field(default=None, alias={definition.name!r}{description})")
    lines.append("")
    return "\n".join(lines)


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
    if definition.external_ranges:
        return f"{item} | list[{item}] | SchemaValue | None"
    return f"{item} | list[{item}] | None"


def _effective_properties(vocabulary: Vocabulary, name: str) -> tuple[str, ...]:
    names = {property_.name for property_ in vocabulary.direct_properties(name)}
    names.update(property_.name for ancestor in vocabulary.ancestry(name) for property_ in vocabulary.direct_properties(ancestor))
    return tuple(sorted(names))


def _render_models_init(models) -> str:
    lines = [
        "from importlib import import_module",
        "",
        "_MODEL_MODULES = {",
    ]
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
        "from schema_org.base import PropertyMetadata",
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
            f"    {definition.name!r}: ({definition.uri!r}, {definition.label!r}, {definition.comment!r}, "
            f"{definition.parents!r}, {definition.external_parents!r}, {definition.equivalent_classes!r}, "
            f"{definition.superseded_by!r}, {definition.supersedes!r}, {definition.contributors!r}, {definition.sources!r}),"
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


def _render_schema_version(version: SchemaVersion, source_hash: str, canonical_hash: str) -> str:
    return (
        f"SCHEMA_VERSION = {version.version!r}\n"
        f"SCHEMA_SOURCE = {version.schema_source!r}\n"
        f"SCHEMA_SOURCE_SHA256 = {source_hash!r}\n"
        f"SCHEMA_VOCABULARY_SHA256 = {canonical_hash!r}\n"
    )


def _render_root_init(vocabulary: Vocabulary) -> str:
    ordinary = sorted(vocabulary.ordinary_classes, key=lambda item: item.name)
    lines = [
        "from importlib import import_module",
        "",
        "from .base import CircularReferenceError, JsonValue, PropertyMetadata, SchemaEnum, SchemaModel, SchemaScalar, SchemaValue",
        "from .schema_version import SCHEMA_VERSION, SCHEMA_SOURCE, SCHEMA_SOURCE_SHA256, SCHEMA_VOCABULARY_SHA256",
        "",
        "_MODEL_MODULES = {",
    ]
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
        "    'SCHEMA_VERSION',", "    'SCHEMA_SOURCE',", "    'SCHEMA_SOURCE_SHA256',",
        "    'SCHEMA_VOCABULARY_SHA256',", "    'SchemaModel',", "    'SchemaEnum',",
        "    'CircularReferenceError',",
        "]",
    ])
    return "\n".join(lines) + "\n"


def _manifest(vocabulary: Vocabulary, version: SchemaVersion, source_hash: str, canonical_hash: str, package: Path) -> dict[str, object]:
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
        "schema_source_sha256": source_hash,
        "schema_vocabulary_sha256": canonical_hash,
        "paths": paths,
        "terms": terms,
    }


def _commit_tree(staged: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.parent.parent
    previous_manifest_path = root / "codegen/generated_manifest.json"
    previous_paths: set[str] = set()
    if previous_manifest_path.exists():
        try:
            loaded = json.loads(previous_manifest_path.read_text(encoding="utf-8"))
            previous_paths = {
                path for path in loaded.get("paths", [])
                if _safe_generated_path(path)
            }
        except (OSError, ValueError):
            previous_paths = set()
    new_paths = {f"src/schema_org/{path.relative_to(staged).as_posix()}" for path in staged.rglob("*") if path.is_file()}
    touched = {root / relative for relative in previous_paths | new_paths}
    with tempfile.TemporaryDirectory(prefix="schema-org-rollback-", dir=root) as backup_dir_name:
        backup_dir = Path(backup_dir_name)
        states: dict[Path, bool] = {}
        for index, path in enumerate(sorted(touched)):
            states[path] = path.exists()
            if path.exists():
                (backup_dir / str(index)).write_bytes(path.read_bytes())
        try:
            for relative in sorted(previous_paths - new_paths):
                target = root / relative
                if target.exists():
                    target.unlink()
            for source in sorted(path for path in staged.rglob("*") if path.is_file()):
                _atomic_replace(source, destination / source.relative_to(staged))
        except BaseException:
            for index, path in enumerate(sorted(touched)):
                backup = backup_dir / str(index)
                if states[path]:
                    _atomic_write(path, backup.read_bytes())
                elif path.exists():
                    path.unlink()
            raise

def _safe_generated_path(path: object) -> bool:
    if not isinstance(path, str) or not path.startswith("src/schema_org/"):
        return False
    relative = PurePosixPath(path)
    return ".." not in relative.parts and len(relative.parts) > 2


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def _atomic_replace(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(source, destination)
