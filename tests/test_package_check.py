import io
import tarfile
import warnings
import zipfile
from pathlib import Path

import pytest
from schema_org_codegen import ValidationError
from schema_org_codegen.package_check import (
    _runtime_files,
    _validate_sdist,
    _validate_wheel,
)


def test_wheel_requires_exact_runtime_and_metadata(tmp_path: Path):
    path = tmp_path / "sample.whl"
    names = [
        "schema_org/__init__.py",
        "schema_org/py.typed",
        "sample-1.0.dist-info/METADATA",
        "sample-1.0.dist-info/WHEEL",
        "sample-1.0.dist-info/RECORD",
        "sample-1.0.dist-info/licenses/LICENSE.txt",
        "sample-1.0.dist-info/licenses/LICENSE-SCHEMA-ORG.txt",
    ]
    with zipfile.ZipFile(path, "w") as archive:
        for name in names:
            archive.writestr(name, b"x")
    _validate_wheel(path, {"__init__.py", "py.typed"})
    with zipfile.ZipFile(path, "a") as archive:
        archive.writestr("schema_org/unexpected.py", b"x")
    with pytest.raises(ValidationError):
        _validate_wheel(path, {"__init__.py", "py.typed"})


def test_sdist_allows_ancestor_directories_and_rejects_development_files(tmp_path: Path):
    path = tmp_path / "sample-1.0.tar.gz"
    root = "sample-1.0"
    files = {
        f"{root}/src/schema_org/__init__.py": b"x",
        f"{root}/src/schema_org/py.typed": b"",
        f"{root}/pyproject.toml": b"x",
        f"{root}/README.md": b"x",
        f"{root}/CHANGELOG.md": b"x",
        f"{root}/LICENSE.txt": b"x",
        f"{root}/LICENSE-SCHEMA-ORG.txt": b"x",
        f"{root}/build_hooks.py": b"x",
        f"{root}/PKG-INFO": b"x",
    }
    with tarfile.open(path, "w:gz") as archive:
        for name, content in files.items():
            info = tarfile.TarInfo(name)
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))
    _validate_sdist(path, {"__init__.py", "py.typed"}, tmp_path)
    bad = tmp_path / "bad-1.0.tar.gz"
    with tarfile.open(bad, "w:gz") as archive:
        for name, content in files.items():
            info = tarfile.TarInfo(name.replace(root, "bad-1.0", 1))
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))
        info = tarfile.TarInfo("bad-1.0/.gitignore")
        archive.addfile(info)
    with pytest.raises(ValidationError):
        _validate_sdist(bad, {"__init__.py", "py.typed"}, tmp_path)


def test_runtime_files_follow_manifest_and_base_only(tmp_path: Path):
    runtime = tmp_path / "src/schema_org"
    (runtime / "__init__.py").parent.mkdir(parents=True)
    (runtime / "__init__.py").write_bytes(b"")
    (runtime / "base.py").write_bytes(b"")
    (tmp_path / "codegen").mkdir()
    manifest = {
        "schema_version": "1.0",
        "schema_source": "https://schema.org/version/1.0/schemaorg-all-https.ttl",
        "paths": ["src/schema_org/__init__.py"],
        "terms": {
            "classes": [],
            "datatypes": [],
            "enumerations": [],
            "enumeration_members": [],
            "properties": [],
        },
    }
    import json
    (tmp_path / "codegen/generated_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    assert _runtime_files(tmp_path) == {"__init__.py", "base.py"}
    (runtime / "unexpected.py").write_bytes(b"")
    with pytest.raises(ValidationError):
        _runtime_files(tmp_path)


def _write_wheel(path: Path, names: list[str]) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        for name in names:
            archive.writestr(name, b"x")


def _write_sdist(path: Path, names: list[str]) -> None:
    with tarfile.open(path, "w:gz") as archive:
        for name in names:
            info = tarfile.TarInfo(name)
            info.size = 1
            archive.addfile(info, io.BytesIO(b"x"))


def test_wheel_rejects_missing_required_entries_and_wrong_root(tmp_path: Path):
    names = [
        "schema_org/__init__.py",
        "schema_org/py.typed",
        "sample-1.0.dist-info/METADATA",
        "sample-1.0.dist-info/WHEEL",
        "sample-1.0.dist-info/RECORD",
        "sample-1.0.dist-info/licenses/LICENSE.txt",
        "sample-1.0.dist-info/licenses/LICENSE-SCHEMA-ORG.txt",
    ]
    for missing in names:
        path = tmp_path / "missing.whl"
        _write_wheel(path, [name for name in names if name != missing])
        with pytest.raises(ValidationError):
            _validate_wheel(path, {"__init__.py", "py.typed"})
    path = tmp_path / "sample-1.0-py3-none-any.whl"
    _write_wheel(
        path,
        [name.replace("sample-1.0.dist-info", "other-1.0.dist-info") for name in names],
    )
    with pytest.raises(ValidationError):
        _validate_wheel(path, {"__init__.py", "py.typed"})


@pytest.mark.parametrize(
    "extra",
    [
        "codegen/generator.py",
        "codegen/data/schema.ttl",
        "tests/test_runtime.py",
        "schema_org/unexpected.py",
    ],
)
def test_wheel_rejects_forbidden_and_unexpected_entries(tmp_path: Path, extra: str):
    path = tmp_path / "sample-1.0.whl"
    names = [
        "schema_org/__init__.py",
        "schema_org/py.typed",
        "sample-1.0.dist-info/METADATA",
        "sample-1.0.dist-info/WHEEL",
        "sample-1.0.dist-info/RECORD",
        "sample-1.0.dist-info/licenses/LICENSE.txt",
        "sample-1.0.dist-info/licenses/LICENSE-SCHEMA-ORG.txt",
        extra,
    ]
    _write_wheel(path, names)
    with pytest.raises(ValidationError):
        _validate_wheel(path, {"__init__.py", "py.typed"})


def test_wheel_rejects_unsafe_and_non_regular_entries(tmp_path: Path):
    path = tmp_path / "sample-1.0.whl"
    names = [
        "schema_org/__init__.py",
        "schema_org/py.typed",
        "sample-1.0.dist-info/METADATA",
        "sample-1.0.dist-info/WHEEL",
        "sample-1.0.dist-info/RECORD",
        "sample-1.0.dist-info/licenses/LICENSE.txt",
        "sample-1.0.dist-info/licenses/LICENSE-SCHEMA-ORG.txt",
    ]
    _write_wheel(path, [*names, "../unsafe"])
    with pytest.raises(ValidationError):
        _validate_wheel(path, {"__init__.py", "py.typed"})

    with zipfile.ZipFile(path, "w") as archive:
        for name in names:
            archive.writestr(name, b"x")
        info = zipfile.ZipInfo("schema_org/link")
        info.external_attr = 0o120777 << 16
        archive.writestr(info, b"x")
    with pytest.raises(ValidationError):
        _validate_wheel(path, {"__init__.py", "py.typed"})


def test_sdist_rejects_missing_required_entries_and_wrong_root(tmp_path: Path):
    root = "sample-1.0"
    names = [
        f"{root}/src/schema_org/__init__.py",
        f"{root}/src/schema_org/py.typed",
        f"{root}/pyproject.toml",
        f"{root}/README.md",
        f"{root}/CHANGELOG.md",
        f"{root}/LICENSE.txt",
        f"{root}/LICENSE-SCHEMA-ORG.txt",
        f"{root}/build_hooks.py",
        f"{root}/PKG-INFO",
    ]
    for missing in names:
        path = tmp_path / "sample-1.0.tar.gz"
        _write_sdist(path, [name for name in names if name != missing])
        with pytest.raises(ValidationError):
            _validate_sdist(path, {"__init__.py", "py.typed"}, tmp_path)

    path = tmp_path / "sample-1.0.tar.gz"
    _write_sdist(path, [name.replace(root, "other-1.0", 1) for name in names])
    with pytest.raises(ValidationError):
        _validate_sdist(path, {"__init__.py", "py.typed"}, tmp_path)


@pytest.mark.parametrize(
    "extra",
    [
        "codegen/generated_manifest.json",
        "codegen/data/schema.ttl",
        "tests/test_runtime.py",
        ".gitignore",
    ],
)
def test_sdist_rejects_forbidden_and_unsafe_entries(tmp_path: Path, extra: str):
    root = "sample-1.0"
    names = [
        f"{root}/src/schema_org/__init__.py",
        f"{root}/src/schema_org/py.typed",
        f"{root}/pyproject.toml",
        f"{root}/README.md",
        f"{root}/CHANGELOG.md",
        f"{root}/LICENSE.txt",
        f"{root}/LICENSE-SCHEMA-ORG.txt",
        f"{root}/build_hooks.py",
        f"{root}/PKG-INFO",
        f"{root}/{extra}",
    ]
    path = tmp_path / "sample-1.0.tar.gz"
    _write_sdist(path, names)
    with pytest.raises(ValidationError):
        _validate_sdist(path, {"__init__.py", "py.typed"}, tmp_path)

    unsafe = tmp_path / "unsafe-1.0.tar.gz"
    _write_sdist(unsafe, [*names[:-1], f"{root}/../escape"])
    with pytest.raises(ValidationError):
        _validate_sdist(unsafe, {"__init__.py", "py.typed"}, tmp_path)


def test_archives_reject_duplicate_and_non_regular_sdist_members(tmp_path: Path):
    wheel = tmp_path / "sample-1.0-py3-none-any.whl"
    names = [
        "schema_org/__init__.py",
        "schema_org/py.typed",
        "sample-1.0.dist-info/METADATA",
        "sample-1.0.dist-info/WHEEL",
        "sample-1.0.dist-info/RECORD",
        "sample-1.0.dist-info/licenses/LICENSE.txt",
        "sample-1.0.dist-info/licenses/LICENSE-SCHEMA-ORG.txt",
    ]
    with zipfile.ZipFile(wheel, "w") as archive:
        for name in names:
            archive.writestr(name, b"x")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            archive.writestr(names[0], b"x")
    with pytest.raises(ValidationError):
        _validate_wheel(wheel, {"__init__.py", "py.typed"})

    sdist = tmp_path / "nonregular-1.0.tar.gz"
    files = [
        "nonregular-1.0/src/schema_org/__init__.py",
        "nonregular-1.0/src/schema_org/py.typed",
        "nonregular-1.0/pyproject.toml",
        "nonregular-1.0/README.md",
        "nonregular-1.0/CHANGELOG.md",
        "nonregular-1.0/LICENSE.txt",
        "nonregular-1.0/LICENSE-SCHEMA-ORG.txt",
        "nonregular-1.0/build_hooks.py",
        "nonregular-1.0/PKG-INFO",
    ]
    with tarfile.open(sdist, "w:gz") as archive:
        for name in files:
            info = tarfile.TarInfo(name)
            info.size = 1
            archive.addfile(info, io.BytesIO(b"x"))
        info = tarfile.TarInfo("nonregular-1.0/socket")
        info.type = tarfile.SYMTYPE
        info.linkname = "/tmp/escape"
        archive.addfile(info)
    with pytest.raises(ValidationError):
        _validate_sdist(sdist, {"__init__.py", "py.typed"}, tmp_path)
