from __future__ import annotations

import json
import re
from pathlib import PurePosixPath

from .path_validation import validate_relative_file_path
from .vocabulary import ValidationError

_MANIFEST_KEYS = frozenset({"schema_version", "schema_source", "paths", "terms"})
_TERM_KEYS = frozenset({"classes", "datatypes", "enumerations", "enumeration_members", "properties"})
_ROOT_FILES = frozenset({
    "src/schema_org/__init__.py",
    "src/schema_org/datatypes.py",
    "src/schema_org/enums.py",
    "src/schema_org/registry.py",
    "src/schema_org/schema_version.py",
    "src/schema_org/py.typed",
    "src/schema_org/models/__init__.py",
})
_VERSION_SOURCE = re.compile(r"https://schema\.org/version/(\d+\.\d+)/schemaorg-all-https\.ttl")


def read_manifest(path: Path, *, project_root: Path | None = None) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        raise ValidationError("generated manifest is invalid") from error
    return validate_manifest(value, project_root=project_root)


def validate_manifest(value: object, *, project_root: Path | None = None) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) != _MANIFEST_KEYS:
        raise ValidationError("generated manifest is invalid")
    version = value.get("schema_version")
    source = value.get("schema_source")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+", version):
        raise ValidationError("generated manifest schema_version is invalid")
    source_match = _VERSION_SOURCE.fullmatch(source) if isinstance(source, str) else None
    if source_match is None or source_match.group(1) != version:
        raise ValidationError("generated manifest schema_source is invalid")
    paths = _sorted_unique_strings(value.get("paths"))
    terms = value.get("terms")
    if not isinstance(terms, dict) or set(terms) != _TERM_KEYS:
        raise ValidationError("generated manifest terms are invalid")
    normalized_terms = {
        key: _sorted_unique_strings(terms.get(key))
        for key in sorted(_TERM_KEYS)
    }
    for path in paths:
        _validate_owned_path(path)
    if project_root is not None:
        _validate_filesystem_paths(project_root, paths)
    return {
        "schema_version": version,
        "schema_source": source,
        "paths": paths,
        "terms": normalized_terms,
    }


def owned_path(path: str) -> bool:
    try:
        _validate_owned_path(path)
    except ValidationError:
        return False
    return True


def _sorted_unique_strings(value: object) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValidationError("generated manifest lists are invalid")
    if value != sorted(value) or len(value) != len(set(value)):
        raise ValidationError("generated manifest lists must be sorted and unique")
    return list(value)


def _validate_owned_path(path: str) -> None:
    pure = validate_relative_file_path(path)
    if path in _ROOT_FILES:
        return
    if pure.match("src/schema_org/models/*.py") and pure.name != "__init__.py":
        return
    raise ValidationError(f"unowned generated path {path!r}")


def _validate_filesystem_paths(root: Path, paths: list[str]) -> None:
    for relative in paths:
        target = root / relative
        current = root
        for part in PurePosixPath(relative).parts:
            current = current / part
            if current.is_symlink():
                raise ValidationError(f"generated path is a symlink: {relative}")
        if target.exists() and not target.is_file():
            raise ValidationError(f"generated path is not a regular file: {relative}")
