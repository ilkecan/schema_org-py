from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .vocabulary import ValidationError

_RELEASE = re.compile(r"# schema_org_release: (v\d+\.\d+)")
_SOURCE = re.compile(r"# schema_org_source: (https://schema\.org/version/(\d+\.\d+)/schemaorg-all-https\.ttl)")


@dataclass(frozen=True, slots=True)
class SchemaVersion:
    schema_version: str
    schema_source: str

    @property
    def version(self) -> str:
        return self.schema_version.removeprefix("v")

    @classmethod
    def current(cls, schema_file: str | Path) -> SchemaVersion:
        try:
            lines = Path(schema_file).read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as error:
            raise ValidationError(f"Unable to read schema file: {schema_file}") from error
        release = _RELEASE.fullmatch(lines[0]) if lines else None
        source = _SOURCE.fullmatch(lines[1]) if len(lines) > 1 else None
        if not release or not source or release.group(1).removeprefix("v") != source.group(2):
            raise ValidationError("Schema file must begin with matching release and source headers")
        if any(_RELEASE.fullmatch(line) or _SOURCE.fullmatch(line) for line in lines[2:]):
            raise ValidationError("Schema file contains duplicate release/source headers")
        return cls(release.group(1), source.group(1))
