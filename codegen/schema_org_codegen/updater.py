from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.request import urlopen
import tempfile

from .generator import generate
from .package_check import validate_distributions
from .manifest import read_manifest
from .check import check
from .schema_version import SchemaVersion
from .transaction import apply_transaction
from .vocabulary import ValidationError, Vocabulary

LATEST_URL = "https://schema.org/version/latest/"
VERSION_PATTERN = re.compile(r"Schema\.org Version\s+(?:v)?(\d+\.\d+)", re.IGNORECASE)


class SchemaUpdater:
    def __init__(self, downloader=None, *, target: str | Path | None = None, project_root: str | Path | None = None, validator=None):
        self.project_root = Path(project_root) if project_root is not None else Path(__file__).resolve().parents[2]
        self.target = Path(target) if target is not None else self.project_root / "codegen/data/schema.ttl"
        self.downloader = downloader or _download
        self.validator = validator

    def latest_version(self) -> str:
        body = _response_body(self._download_checked(LATEST_URL))
        match = VERSION_PATTERN.search(body)
        if not match:
            raise ValidationError("could not parse Schema.org Version from latest release page")
        return match.group(1)

    def _download_checked(self, url: str):
        try:
            return self.downloader(url)
        except ValidationError:
            raise
        except Exception as error:
            raise ValidationError(f"failed to download {url}: {error}") from error

    def update(self, version: str | None = None) -> bool:
        numeric = _numeric_version(version) if version is not None else self.latest_version()
        current = SchemaVersion.current(self.target)
        if numeric == current.version:
            return False
        url = f"https://schema.org/version/{numeric}/schemaorg-all-https.ttl"
        body_bytes = _response_bytes(self._download_checked(url))
        if not body_bytes:
            raise ValidationError("schema download was empty")
        try:
            body = body_bytes.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValidationError("schema download was not valid UTF-8") from error
        annotated = (
            f"# schema_org_release: v{numeric}\n"
            f"# schema_org_source: {url}\n"
            f"{body}"
        )
        with tempfile.TemporaryDirectory(prefix="schema-org-update-", dir=self.project_root) as temporary:
            staging = Path(temporary)
            validation_root = self._validation_root(staging)
            candidate = validation_root / "codegen/data/schema.ttl"
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_text(annotated, encoding="utf-8")
            candidate_version = SchemaVersion.current(candidate)
            if candidate_version.version != numeric:
                raise ValidationError("downloaded schema version mismatch")
            try:
                vocabulary = Vocabulary.from_file(candidate)
            except ValidationError:
                raise
            except Exception as error:
                raise ValidationError(f"downloaded schema could not be parsed: {error}") from error
            if not vocabulary.subjects:
                raise ValidationError("downloaded schema could not be parsed")
            generate(candidate, project_root=validation_root, output_root=validation_root)
            self._validate_staged(validation_root)
            if self.validator is not None:
                self.validator(validation_root)
            self._commit(validation_root, annotated)
        return True

    def _validation_root(self, staging: Path) -> Path:
        if not (self.project_root / "pyproject.toml").exists():
            root = staging / "project"
            root.mkdir()
            return root
        root = staging / "project"
        shutil.copytree(self.project_root, root, ignore=_ignore_validation_files)
        return root
    def _validate_staged(self, root: Path) -> None:
        package = root / "src/schema_org"
        for path in package.rglob("*.py"):
            result = subprocess.run([sys.executable, "-m", "py_compile", str(path)], capture_output=True, text=True)
            if result.returncode:
                raise ValidationError(f"generated Python failed to compile: {result.stderr.strip()}")
        if (root / "tests").is_dir() and (root / "pyproject.toml").exists():
            environment = os.environ.copy()
            environment["PYTHONPATH"] = f"{root / 'src'}:{root / 'codegen'}"
            _run_checked([sys.executable, "-m", "pytest"], root, environment, "generated tests failed")
        if (root / "codegen/generated_manifest.json").exists():
            check(root)
        if (root / "pyproject.toml").exists():
            build_dir = root / ".schema-org-build"
            _run_checked([sys.executable, "-m", "build", "--outdir", str(build_dir)], root, os.environ.copy(), "generated package build failed")
            validate_distributions(build_dir, project_root=root)

    def _commit(self, staging: Path, annotated: str) -> None:
        staged_package = staging / "src/schema_org"
        manifest_target = self.project_root / "codegen/generated_manifest.json"
        staged_manifest_path = staging / "codegen/generated_manifest.json"
        staged_manifest = read_manifest(staged_manifest_path, project_root=staging)
        previous_manifest = read_manifest(manifest_target, project_root=self.project_root)
        old_paths = set(previous_manifest["paths"])
        new_paths = set(staged_manifest["paths"])
        replacements = {
            relative: (staged_package / Path(relative).relative_to("src/schema_org")).read_bytes()
            for relative in sorted(new_paths)
        }
        replacements[manifest_target.relative_to(self.project_root).as_posix()] = staged_manifest_path.read_bytes()
        replacements[self.target.relative_to(self.project_root).as_posix()] = annotated.encode("utf-8")
        apply_transaction(self.project_root, replacements, old_paths - new_paths, writer=_atomic_write_bytes)

def _ignore_validation_files(path: str, names: list[str]) -> set[str]:
    ignored = {".git", ".devenv", ".pytest_cache", "__pycache__", ".venv", "dist", "build"}
    return {name for name in names if name in ignored or name.startswith("tmp") or name.startswith(".schema-org-")}


def _run_checked(command: list[str], cwd: Path, environment: dict[str, str], message: str) -> None:
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise ValidationError(f"{message}: {detail}")








def _atomic_write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    os.replace(temporary, path)

def _numeric_version(version: str) -> str:
    match = re.fullmatch(r"v?(\d+\.\d+)", str(version))
    if not match:
        raise ValidationError("expected schema version v<major>.<minor>")
    return match.group(1)


def _response_body(response) -> str:
    return _response_bytes(response).decode("utf-8")


def _response_bytes(response) -> bytes:
    status = getattr(response, "status", getattr(response, "status_code", None))
    if status is not None and not 200 <= int(status) < 300:
        raise ValidationError(f"failed to download schema: {status}")
    code = getattr(response, "code", None)
    if code is not None and not 200 <= int(code) < 300:
        raise ValidationError(f"failed to download schema: {code}")
    if hasattr(response, "body"):
        body = response.body
    elif hasattr(response, "text"):
        body = response.text
    elif hasattr(response, "content"):
        body = response.content
    else:
        body = response
    if isinstance(body, bytes):
        return body
    return str(body).encode("utf-8")


def _download(url: str):
    with urlopen(url) as response:
        return response.read()
