from datetime import date

from schema_org import ItemAvailability, Offer, Person, SchemaModel
from schema_org.base import JsonValue
from schema_org.enums import GenderType
from schema_org.models.postal_address import PostalAddress


def accepts_model(value: SchemaModel) -> SchemaModel:
    return value


PERSON_TYPE: type[Person] = Person
GENDER_TYPE: type[GenderType] = GenderType
ADDRESS_TYPE: type[PostalAddress] = PostalAddress


def build_person() -> Person:
    person = Person(
        name="Ada",
        birth_date=date(1815, 12, 10),
        address=PostalAddress(address_locality="London"),
        colleague=["https://example.test/charles"],
    )
    person.job_title = "Mathematician"
    person.gender = "https://schema.org/Female"
    person.children = Person(name="Byron")
    return person


def build_offer() -> Offer:
    return Offer(availability=ItemAvailability.IN_STOCK)


def serialize_model(value: SchemaModel) -> dict[str, JsonValue]:
    return value.to_jsonld()
