# schema-org

`schema-org` provides generated Pydantic 2 models for the Schema.org vocabulary.

## Installation

```sh
pip install schema-org
```

## Usage

```python
from schema_org import Person, PostalAddress

person = Person(
    name="Jane Doe",
    address=PostalAddress(address_locality="Seattle"),
)
print(person.to_jsonld())
```

Models use strict validation, Schema.org aliases, and JSON-LD serialization. The checked-in vocabulary version is exposed as `schema_org.SCHEMA_VERSION`.

## Licensing and attribution

Project-authored material and generated Python structure are offered under the MIT License. The Schema.org vocabulary snapshot and descriptions derived from it remain licensed under CC BY-SA 3.0. See `LICENSE.txt` and `LICENSE-SCHEMA-ORG.txt`.
