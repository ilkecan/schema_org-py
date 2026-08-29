from pathlib import Path

import pytest

from schema_org_codegen.transaction import TransactionError, apply_transaction
from schema_org_codegen import ValidationError


def files(root: Path):
    return {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}


def test_transaction_skips_unchanged_and_rolls_back_new_files(tmp_path: Path):
    (tmp_path / "same").write_bytes(b"same")
    before = files(tmp_path)
    calls = 0

    def writer(path: Path, content: bytes):
        nonlocal calls
        calls += 1
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        if calls == 2:
            raise OSError("one-shot failure")

    with pytest.raises(OSError):
        apply_transaction(tmp_path, {"same": b"same", "new": b"new", "other": b"other"}, writer=writer)
    assert files(tmp_path) == before


@pytest.mark.parametrize(
    "relative",
    [
        "../escape",
        "/absolute",
        "dir/../escape",
        "dir/./file",
        "dir//file",
        "dir/file/",
        r"dir\file",
        "C:/file",
    ],
)
def test_transaction_rejects_each_unsafe_path(tmp_path: Path, relative: str):
    with pytest.raises(ValidationError):
        apply_transaction(tmp_path, {relative: b"x"})


@pytest.mark.parametrize("relative", ["src//schema_org/models/person.py", "src/schema_org/models/person.py/", r"src\schema_org\models\person.py"])
def test_manifest_rejects_noncanonical_owned_paths(relative: str):
    from schema_org_codegen.manifest import validate_manifest

    value = {
        "schema_version": "1.0",
        "schema_source": "https://schema.org/version/1.0/schemaorg-all-https.ttl",
        "paths": [relative],
        "terms": {
            "classes": [],
            "datatypes": [],
            "enumerations": [],
            "enumeration_members": [],
            "properties": [],
        },
    }
    with pytest.raises(ValidationError):
        validate_manifest(value)


def test_transaction_rolls_back_removal_and_replacement(tmp_path: Path):
    (tmp_path / "remove").write_bytes(b"remove")
    (tmp_path / "replace").write_bytes(b"old")
    before = files(tmp_path)
    calls = 0

    def writer(path: Path, content: bytes):
        nonlocal calls
        calls += 1
        path.write_bytes(content)
        if calls == 1:
            raise OSError("replace failed")

    with pytest.raises(OSError):
        apply_transaction(tmp_path, {"replace": b"new"}, ["remove"], writer=writer)
    assert files(tmp_path) == before

def test_transaction_rejects_unsafe_and_symlink_paths(tmp_path: Path):
    with pytest.raises(ValidationError):
        apply_transaction(tmp_path, {"../escape": b"x"})
    (tmp_path / "real").mkdir()
    (tmp_path / "link").symlink_to(tmp_path / "real", target_is_directory=True)
    with pytest.raises(ValidationError):
        apply_transaction(tmp_path, {"link/file": b"x"})


def test_transaction_reports_restoration_failure(tmp_path: Path):
    (tmp_path / "value").write_bytes(b"old")
    calls = 0

    def writer(path: Path, content: bytes):
        nonlocal calls
        calls += 1
        path.write_bytes(content)
        raise OSError("failure")

    with pytest.raises(TransactionError, match="restoration failed"):
        apply_transaction(tmp_path, {"value": b"new"}, writer=writer)
