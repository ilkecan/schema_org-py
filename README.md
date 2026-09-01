# schema-org

`schema-org` provides generated Pydantic 2 models for the Schema.org vocabulary. The package version is `0.1.0`; the checked-in vocabulary version is exposed as `schema_org.SCHEMA_VERSION`.

## Installation

```sh
pip install schema-org==0.1.0
```

## Supported Python versions

The package supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.

## Usage

Construct generated models with `snake_case` properties. Values are checked on construction and assignment.

Schema.org type names generally map directly to Python class names. The exception in the current vocabulary is `3DModel`, which is exposed as `ThreeDModel` because Python identifiers cannot begin with a digit.

```python
from datetime import date

from schema_org import Person, PostalAddress

person = Person(
    name="Jane Doe",
    job_title="Professor",
    birth_date=date(1980, 1, 2),
    address=PostalAddress(address_locality="Seattle"),
    colleague=["https://example.test/alice", "https://example.test/bob"],
)
person.job_title = "Researcher"
person.birth_date = None

person.to_jsonld()
# {
#     "@context": "https://schema.org",
#     "@type": "Person",
#     "address": {
#         "@type": "PostalAddress",
#         "addressLocality": "Seattle",
#     },
#     "colleague": [
#         "https://example.test/alice",
#         "https://example.test/bob",
#     ],
#     "jobTitle": "Researcher",
#     "name": "Jane Doe",
# }
person.to_jsonld_json(indent=2)
```

Schema.org aliases can also be used as validation input. Models use strict Pydantic validation, reject unknown fields, and validate assignment.

Enumeration values are generated enum members:

```python
from schema_org import ItemAvailability, Offer

offer = Offer(availability=ItemAvailability.IN_STOCK)
offer.to_jsonld_json()  # includes https://schema.org/InStock
```

`to_jsonld()` returns a string-keyed JSON-LD dictionary. `to_jsonld_json()` returns the corresponding JSON string. Only the root object includes `@context`; nested schema values are serialized recursively. Lists and native `date`, `datetime`, and `time` values are supported.

## Typing and metadata

The package includes `py.typed` and generated annotations for the complete checked-in vocabulary. Models and enumerations are available from `schema_org` and from their generated modules.

Generated models expose `SCHEMA_TYPE`, `SCHEMA_TYPES`, and frozen `SCHEMA_PROPERTIES`. Each `PropertyMetadata` value includes the Schema.org name, URL, accepted ranges, relationships, and source `comment`.

## Development

```sh
uv sync --locked
uv run python -m pytest
uv run ruff check .
uv run ty check
uv run python -m schema_org_codegen.check
uv run python -m build --outdir dist
uv run python -m schema_org_codegen.package_check "$PWD/dist"
```

The schema generator and its source data live in `codegen/`. Generated runtime files live in `src/schema_org/`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for pull request contribution and verification procedures. See [MAINTAINING.md](MAINTAINING.md) for Schema.org update and release procedures.

## Licensing and attribution

Project-authored material and generated Python structure are offered under the [MIT License](LICENSE.txt). The complete `codegen/data/schema.ttl` snapshot and Schema.org descriptions copied into generated docstrings and metadata remain licensed under [CC BY-SA 3.0](LICENSE-SCHEMA-ORG.txt). The snapshot is maintainer input and is not included in the distribution.
