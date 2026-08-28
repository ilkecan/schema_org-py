from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .vocabulary import ValidationError

_RELEASE = re.compile(r"# schema_org_release: (v\d+\.\d+)\n")
_SOURCE = re.compile(r"# schema_org_source: (https://schema\.org/version/(\d+\.\d+)/schemaorg-all-https\.ttl)\n")
_SOURCE_SHA256 = re.compile(r"# schema_org_source_sha256: ([0-9a-f]{64})\n")


@dataclass(frozen=True, slots=True)
class SchemaVersion:
    schema_version: str
    schema_source: str
    source_sha256: str | None = None

    @property
    def version(self) -> str:
        return self.schema_version.removeprefix("v")

    @classmethod
    def current(cls, schema_file: str | Path) -> "SchemaVersion":
        try:
            content = Path(schema_file).read_text(encoding="utf-8")
        except OSError as error:
            raise ValidationError(f"Unable to read schema file: {schema_file}") from error
        release = _RELEASE.match(content)
        source = _SOURCE.match(content, release.end() if release else 0)
        if not release or not source:
            raise ValidationError("Schema file must begin with release and source headers in order")
        if content.count("schema_org_release:") != 1 or content.count("schema_org_source:") != 1:
            raise ValidationError("Schema release and source headers must be unique")
        if release.group(1).removeprefix("v") != source.group(2):
            raise ValidationError("Schema release and source versions do not match")
        source_sha = _SOURCE_SHA256.match(content, source.end())
        if source_sha is not None and content.count("schema_org_source_sha256:") != 1:
            raise ValidationError("Schema source hash header must be unique")
        return cls(release.group(1), source.group(1), source_sha.group(1) if source_sha else None)
