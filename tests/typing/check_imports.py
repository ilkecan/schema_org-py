from schema_org import Person, SchemaModel
from schema_org.enums import GenderType
from schema_org.models.postal_address import PostalAddress


def accepts_model(value: SchemaModel) -> SchemaModel:
    return value


PERSON_TYPE: type[Person] = Person
GENDER_TYPE: type[GenderType] = GenderType
ADDRESS_TYPE: type[PostalAddress] = PostalAddress
