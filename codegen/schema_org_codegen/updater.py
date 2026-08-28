from __future__ import annotations

import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
from typing import cast
import tarfile
import zipfile
from urllib.request import urlopen

from .generator import generate
from .schema_version import SchemaVersion
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
        if (root / "pyproject.toml").exists():
            build_dir = root / ".schema-org-build"
            _run_checked([sys.executable, "-m", "build", "--outdir", str(build_dir)], root, os.environ.copy(), "generated package build failed")
            for artifact in build_dir.iterdir():
                if artifact.suffix not in {".whl", ".gz", ".zip"}:
                    raise ValidationError(f"unexpected build artifact {artifact.name}")
                _validate_archive(artifact)

    def _commit(self, staging: Path, annotated: str) -> None:
        staged_package = staging / "src/schema_org"
        destination = self.project_root / "src/schema_org"
        manifest_target = self.project_root / "codegen/generated_manifest.json"
        previous_manifest = _read_manifest(manifest_target)
        old_paths = {
            path for path in cast(list[object], previous_manifest.get("paths", []))
            if _safe_generated_path(path)
        }
        new_paths = {
            f"src/schema_org/{path.relative_to(staged_package).as_posix()}"
            for path in staged_package.rglob("*") if path.is_file()
        }
        touched = {self.target, manifest_target}
        touched.update(self.project_root / path for path in old_paths | new_paths)
        with tempfile.TemporaryDirectory(prefix="schema-org-rollback-", dir=self.project_root) as backup_dir_name:
            backup_dir = Path(backup_dir_name)
            states: dict[Path, bool] = {}
            for index, path in enumerate(sorted(touched)):
                states[path] = path.exists()
                if path.exists():
                    (backup_dir / str(index)).write_bytes(path.read_bytes())
            try:
                _atomic_write_bytes(self.target, annotated.encode("utf-8"))
                for relative in sorted(old_paths - new_paths):
                    path = self.project_root / relative
                    if path.exists():
                        path.unlink()
                for source in sorted(path for path in staged_package.rglob("*") if path.is_file()):
                    _atomic_write_bytes(destination / source.relative_to(staged_package), source.read_bytes())
                staged_manifest = staging / "codegen/generated_manifest.json"
                _atomic_write_bytes(manifest_target, staged_manifest.read_bytes())
            except BaseException:
                for index, path in enumerate(sorted(touched)):
                    backup = backup_dir / str(index)
                    if states[path]:
                        _atomic_write_bytes(path, backup.read_bytes())
                    elif path.exists():
                        path.unlink()
                raise


def _safe_generated_path(path: object) -> bool:
    if not isinstance(path, str) or not path.startswith("src/schema_org/"):
        return False
    relative = PurePosixPath(path)
    return ".." not in relative.parts and len(relative.parts) > 2

def _ignore_validation_files(path: str, names: list[str]) -> set[str]:
    ignored = {".git", ".devenv", ".pytest_cache", "__pycache__", ".venv", "dist", "build"}
    return {name for name in names if name in ignored or name.startswith("tmp") or name.startswith(".schema-org-")}


def _run_checked(command: list[str], cwd: Path, environment: dict[str, str], message: str) -> None:
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise ValidationError(f"{message}: {detail}")


def _read_manifest(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValidationError("generated manifest is invalid") from error
    if not isinstance(value, dict) or not isinstance(value.get("paths", []), list):
        raise ValidationError("generated manifest is invalid")
    return value


def _validate_archive(path: Path) -> None:
    if path.suffix == ".whl":
        names = zipfile.ZipFile(path).namelist()
    else:
        names = tarfile.open(path).getnames()
    forbidden = (
        lambda name: "/codegen/" in f"/{name}" or "/tests/" in f"/{name}"
        or name.endswith(".ttl") or "templates" in name
    )
    if any(forbidden(name) for name in names):
        raise ValidationError(f"forbidden development file in {path.name}")
    if path.suffix == ".whl" and not any(name.endswith("py.typed") for name in names):
        raise ValidationError("wheel does not contain py.typed")


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
