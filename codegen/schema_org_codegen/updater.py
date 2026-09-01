from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.request import urlopen

from .check import check
from .generator import generate
from .manifest import read_manifest
from .package_check import validate_distributions
from .schema_version import SchemaVersion
from .transaction import apply_transaction
from .vocabulary import ValidationError, Vocabulary

LATEST_URL = "https://schema.org/version/latest/"
VERSION_PATTERN = re.compile(r"Schema\.org Version\s+(?:v)?(\d+\.\d+)", re.IGNORECASE)


class SchemaUpdater:
    def __init__(self, downloader=None, *, target: str | Path | None = None, project_root: str | Path | None = None, validator=None):
        self.project_root = (Path(project_root) if project_root is not None else Path(__file__).resolve().parents[2]).resolve()
        raw_target = Path(target) if target is not None else Path("codegen/data/schema.ttl")
        candidate = raw_target if raw_target.is_absolute() else self.project_root / raw_target
        self._target_relative = _target_relative(self.project_root, candidate)
        self.target = self.project_root / self._target_relative
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
        current_key = _version_key(current.version)
        requested_key = _version_key(numeric)
        if requested_key == current_key:
            return False
        if requested_key < current_key:
            raise ValidationError("requested schema version is older than the current version")
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
        with tempfile.TemporaryDirectory(prefix="schema-org-update-") as temporary:
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
        required = (
            "pyproject.toml",
            "tests",
            "src/schema_org",
            "codegen",
            "README.md",
            "CHANGELOG.md",
            "LICENSE.txt",
            "LICENSE-SCHEMA-ORG.txt",
            "build_hooks.py",
        )
        if any(not (self.project_root / item).exists() for item in required):
            raise ValidationError("project root is incomplete for schema update validation")
        root = staging / "project"
        shutil.copytree(self.project_root, root, ignore=_ignore_validation_files)
        return root

    def _validate_staged(self, root: Path) -> None:
        package = root / "src/schema_org"
        generated_files = sorted(package.rglob("*.py"))
        if not generated_files:
            raise ValidationError("staged generated package is missing")
        for path in generated_files:
            result = subprocess.run([sys.executable, "-m", "py_compile", str(path)], capture_output=True, text=True)
            if result.returncode:
                raise ValidationError(f"generated Python failed to compile: {result.stderr.strip()}")
        environment = os.environ.copy()
        environment["PYTHONPATH"] = f"{root / 'src'}:{root / 'codegen'}"
        _run_checked([sys.executable, "-m", "pytest"], root, environment, "generated tests failed")
        check(root)
        build_dir = Path(tempfile.mkdtemp(prefix="schema-org-build-"))
        try:
            _run_checked(
                [sys.executable, "-m", "build", "--outdir", str(build_dir)],
                root,
                environment,
                "generated package build failed",
            )
            validate_distributions(build_dir, project_root=root)
        finally:
            shutil.rmtree(build_dir, ignore_errors=True)

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
        replacements["codegen/generated_manifest.json"] = staged_manifest_path.read_bytes()
        replacements[self._target_relative] = annotated.encode("utf-8")
        apply_transaction(self.project_root, replacements, old_paths - new_paths)
def _ignore_validation_files(path: str, names: list[str]) -> set[str]:
    ignored = {".git", ".devenv", ".pytest_cache", "__pycache__", ".venv", "dist", "build"}
    return {name for name in names if name in ignored or name.startswith("tmp") or name.startswith(".schema-org-")}


def _run_checked(command: list[str], cwd: Path, environment: dict[str, str], message: str) -> None:
    result = subprocess.run(command, cwd=cwd, env=environment, capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise ValidationError(f"{message}: {detail}")









def _numeric_version(version: str) -> str:
    match = re.fullmatch(r"v?(\d+\.\d+)", str(version))
    if not match:
        raise ValidationError("expected schema version v<major>.<minor>")
    return match.group(1)


def _response_body(response) -> str:
    try:
        return _response_bytes(response).decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValidationError("schema response was not valid UTF-8") from error

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
def _version_key(version: str) -> tuple[int, int]:
    major, minor = version.split(".", 1)
    return int(major), int(minor)


def _target_relative(project_root: Path, target: Path) -> str:
    candidate = target if target.is_absolute() else project_root / target
    current = project_root
    try:
        relative = candidate.relative_to(project_root)
    except ValueError as error:
        raise ValidationError("schema target must be inside the project root") from error
    if any(part in {".", ".."} for part in relative.parts):
        raise ValidationError("schema target path is unsafe")
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise ValidationError("schema target must not use symlinks")
    return relative.as_posix()
