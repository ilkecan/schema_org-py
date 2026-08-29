from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
from typing import cast
from .generator import generate
from .manifest import read_manifest


def check(project_root: str | Path | None = None) -> None:
    root = Path(project_root) if project_root is not None else Path(__file__).resolve().parents[2]
    manifest_path = root / "codegen/generated_manifest.json"
    current_manifest = read_manifest(manifest_path, project_root=root)
    managed_paths = set(cast(list[str], current_manifest["paths"]))
    actual_models = {
        path.relative_to(root).as_posix()
        for path in (root / "src/schema_org/models").glob("*.py")
    }
    if actual_models - {path for path in managed_paths if path.startswith("src/schema_org/models/")}:
        raise SystemExit("unowned generated model artifact")
    with tempfile.TemporaryDirectory(prefix="schema-org-check-", dir=root) as temporary:
        temporary_root = Path(temporary)
        generate(root / "codegen/data/schema.ttl", project_root=temporary_root, output_root=temporary_root)
        expected_manifest = read_manifest(temporary_root / "codegen/generated_manifest.json", project_root=temporary_root)
        if current_manifest != expected_manifest:
            raise SystemExit("generated manifest drift")
        for relative in managed_paths:
            actual = root / relative
            expected = temporary_root / relative
            if not actual.exists() or _sha256(actual) != _sha256(expected):
                raise SystemExit(f"generated file drift: {relative}")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    check()
