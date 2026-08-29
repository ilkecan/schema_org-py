from __future__ import annotations

from pathlib import PurePosixPath

from .vocabulary import ValidationError


def validate_relative_file_path(relative: str) -> PurePosixPath:
    if not isinstance(relative, str) or not relative:
        raise ValidationError(f"unsafe relative path {relative!r}")
    if "\\" in relative or "//" in relative or relative.endswith("/"):
        raise ValidationError(f"noncanonical relative path {relative!r}")
    if ":" in relative.split("/", 1)[0]:
        raise ValidationError(f"unsafe relative path {relative!r}")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or "." in pure.parts or ".." in pure.parts:
        raise ValidationError(f"unsafe relative path {relative!r}")
    if pure.as_posix() != relative:
        raise ValidationError(f"noncanonical relative path {relative!r}")
    return pure
