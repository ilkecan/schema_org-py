from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile

from .generator import generate


def check(project_root: str | Path | None = None) -> None:
    root = Path(project_root) if project_root is not None else Path(__file__).resolve().parents[2]
    manifest_path = root / "codegen/generated_manifest.json"
    current_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="schema-org-check-", dir=root) as temporary:
        temporary_root = Path(temporary)
        generate(root / "codegen/data/schema.ttl", project_root=temporary_root, output_root=temporary_root)
        expected_manifest = json.loads((temporary_root / "codegen/generated_manifest.json").read_text(encoding="utf-8"))
        if current_manifest != expected_manifest:
            raise SystemExit("generated manifest drift")
        for relative in current_manifest["paths"]:
            actual = root / relative
            expected = temporary_root / relative
            if not actual.exists() or _sha256(actual) != _sha256(expected):
                raise SystemExit(f"generated file drift: {relative}")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    check()
