from pathlib import Path
import io
import tarfile
import zipfile

import pytest

from schema_org_codegen import ValidationError
from schema_org_codegen.package_check import _validate_sdist, _validate_wheel


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
