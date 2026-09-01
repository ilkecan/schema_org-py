from __future__ import annotations

import os
import tempfile
from collections.abc import Iterable, Mapping
from contextlib import suppress
from pathlib import Path

from .path_validation import validate_relative_file_path
from .vocabulary import ValidationError


class TransactionError(RuntimeError):
    pass


def apply_transaction(
    project_root: Path,
    replacements: Mapping[str, bytes],
    removals: Iterable[str] = (),
    *,
    writer=None,
    remover=None,
) -> None:
    writer = _replace_bytes if writer is None else writer
    remover = _remove_path if remover is None else remover
    replacement_paths = set(replacements)
    removal_paths = set(removals)
    if replacement_paths & removal_paths:
        raise ValidationError("transaction path is both replaced and removed")
    relative_paths = replacement_paths | removal_paths
    paths = {relative: _checked_path(project_root, relative) for relative in relative_paths}
    originals: dict[str, bytes | None] = {}
    for relative, path in paths.items():
        if path.exists():
            if path.is_symlink() or not path.is_file():
                raise ValidationError(f"transaction target is not a regular file: {relative}")
            originals[relative] = path.read_bytes()
        else:
            originals[relative] = None
    changed_replacements = {
        relative: content
        for relative, content in replacements.items()
        if originals[relative] != content
    }
    changed_removals = {relative for relative in removal_paths if originals[relative] is not None}
    attempted: set[str] = set()
    try:
        for relative in sorted(changed_removals):
            attempted.add(relative)
            remover(paths[relative])
        for relative in sorted(changed_replacements):
            attempted.add(relative)
            writer(paths[relative], replacements[relative])
    except Exception:
        try:
            _restore(paths, originals, writer, remover, attempted)
        except Exception as restore_error:
            raise TransactionError(f"transaction failed and restoration failed: {restore_error}") from restore_error
        raise


def _checked_path(root: Path, relative: str) -> Path:
    pure = validate_relative_file_path(relative)
    path = root / pure
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            raise ValidationError(f"transaction path is a symlink: {relative}")
    return path


def _replace_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            with suppress(FileNotFoundError):
                temporary.unlink()

def _remove_path(path: Path) -> None:
    path.unlink()

def _restore(
    paths: Mapping[str, Path],
    originals: Mapping[str, bytes | None],
    writer,
    remover,
    attempted: Iterable[str],
) -> None:
    for relative in attempted:
        content = originals[relative]
        path = paths[relative]
        if content is None:
            if path.exists() or path.is_symlink():
                remover(path)
        else:
            writer(path, content)
