from pathlib import Path

import pytest
from schema_org_codegen import ValidationError
from schema_org_codegen.schema_version import SchemaVersion

VALID = (
    "# schema_org_release: v30.0\n"
    "# schema_org_source: https://schema.org/version/30.0/schemaorg-all-https.ttl\n"
)


def test_schema_version_accepts_matching_headers(tmp_path: Path):
    path = tmp_path / "schema.ttl"
    path.write_text(VALID, encoding="utf-8")
    result = SchemaVersion.current(path)
    assert result.schema_version == "v30.0"
    assert result.schema_source.endswith("/30.0/schemaorg-all-https.ttl")


@pytest.mark.parametrize(
    "content",
    [
        "",
        "# schema_org_release: v30.0\n",
        VALID.replace("release", "source", 1),
        VALID + "# schema_org_release: v30.0\n",
        VALID.replace("v30.0", "30.0", 1),
        VALID.replace("https://", "http://"),
        VALID.replace("/30.0/", "/29.0/"),
    ],
)
def test_schema_version_rejects_invalid_headers(tmp_path: Path, content: str):
    path = tmp_path / "schema.ttl"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ValidationError):
        SchemaVersion.current(path)


def test_schema_version_rejects_non_utf8_and_missing_file(tmp_path: Path):
    path = tmp_path / "schema.ttl"
    path.write_bytes(b"\xff")
    with pytest.raises(ValidationError):
        SchemaVersion.current(path)
    with pytest.raises(ValidationError):
        SchemaVersion.current(tmp_path / "missing.ttl")
