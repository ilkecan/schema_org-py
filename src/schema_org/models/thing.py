# Generated Python code is licensed under MIT.
# Schema.org descriptions are licensed under CC BY-SA 3.0.
# See LICENSE-SCHEMA-ORG.txt.

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import Field

from schema_org.base import PropertyMetadata, SchemaModel

if TYPE_CHECKING:
    from schema_org.datatypes import URL, Text
    from schema_org.models import (
        Action,
        CreativeWork,
        Event,
        ImageObject,
        Organization,
        Person,
        PropertyValue,
        TextObject,
    )


class Thing(SchemaModel):
    __doc__ = 'https://schema.org/Thing\n\nThe most generic type of item.'
    SCHEMA_TYPE: ClassVar[str] = 'Thing'
    SCHEMA_TYPES: ClassVar[tuple[str, ...]] = ('Thing',)
    SCHEMA_PROPERTIES: ClassVar[tuple[PropertyMetadata, ...]] = (
        PropertyMetadata(name='additional_type', schema_name='additionalType', schema_url='https://schema.org/additionalType', ranges=('Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('http://www.w3.org/1999/02/22-rdf-syntax-ns#type',), domains=('Thing',), external_domains=(), comment='An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the\n    use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org <a href="https://schema.org/docs/styleguide.html">style guide</a>.', label='additionalType', contributors=(), sources=()),
        PropertyMetadata(name='alternate_name', schema_name='alternateName', schema_url='https://schema.org/alternateName', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='An alias for the item.', label='alternateName', contributors=(), sources=()),
        PropertyMetadata(name='description', schema_name='description', schema_url='https://schema.org/description', ranges=('Text', 'TextObject'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#description', 'http://purl.org/dc/terms/description', 'https://ref.gs1.org/voc/description'), subproperty_of=(), domains=('Thing',), external_domains=(), comment='A description of the item.', label='description', contributors=(), sources=()),
        PropertyMetadata(name='disambiguating_description', schema_name='disambiguatingDescription', schema_url='https://schema.org/disambiguatingDescription', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('description',), domains=('Thing',), external_domains=(), comment='A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.', label='disambiguatingDescription', contributors=(), sources=()),
        PropertyMetadata(name='identifier', schema_name='identifier', schema_url='https://schema.org/identifier', ranges=('PropertyValue', 'Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://purl.org/dc/terms/identifier', 'https://www.omg.org/spec/Commons/Identifiers/identifiedBy'), subproperty_of=(), domains=('Thing',), external_domains=(), comment='The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.\n        ', label='identifier', contributors=(), sources=()),
        PropertyMetadata(name='image', schema_name='image', schema_url='https://schema.org/image', ranges=('ImageObject', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#image',), subproperty_of=(), domains=('Thing',), external_domains=(), comment='An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].', label='image', contributors=(), sources=()),
        PropertyMetadata(name='main_entity_of_page', schema_name='mainEntityOfPage', schema_url='https://schema.org/mainEntityOfPage', ranges=('CreativeWork', 'URL'), external_ranges=(), inverse_of='mainEntity', superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.', label='mainEntityOfPage', contributors=(), sources=()),
        PropertyMetadata(name='name', schema_name='name', schema_url='https://schema.org/name', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#title', 'http://purl.org/dc/terms/title', 'https://www.omg.org/spec/Commons/Text/hasName'), subproperty_of=('http://www.w3.org/2000/01/rdf-schema#label',), domains=('Thing',), external_domains=(), comment='The name of the item.', label='name', contributors=(), sources=()),
        PropertyMetadata(name='owner', schema_name='owner', schema_url='https://schema.org/owner', ranges=('Organization', 'Person'), external_ranges=(), inverse_of='owns', superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='A person or organization who owns this Thing.', label='owner', contributors=(), sources=('https://github.com/schemaorg/schemaorg/issues/4603',)),
        PropertyMetadata(name='potential_action', schema_name='potentialAction', schema_url='https://schema.org/potentialAction', ranges=('Action',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment="Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.", label='potentialAction', contributors=(), sources=()),
        PropertyMetadata(name='same_as', schema_name='sameAs', schema_url='https://schema.org/sameAs', ranges=('URL',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.", label='sameAs', contributors=(), sources=()),
        PropertyMetadata(name='subject_of', schema_name='subjectOf', schema_url='https://schema.org/subjectOf', ranges=('CreativeWork', 'Event'), external_ranges=(), inverse_of='about', superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='A CreativeWork or Event about this Thing.', label='subjectOf', contributors=(), sources=('https://github.com/schemaorg/schemaorg/issues/1670',)),
        PropertyMetadata(name='url', schema_name='url', schema_url='https://schema.org/url', ranges=('URL',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#url',), subproperty_of=(), domains=('Thing',), external_domains=(), comment='URL of the item.', label='url', contributors=(), sources=()),
    )
    schema_id: str | None = Field(default=None, alias='@id')
    schema_type: Literal['Thing'] = Field(default='Thing', alias='@type', frozen=True)
    additional_type: Text | URL | list[Text | URL] | None = Field(default=None, alias='additionalType', description='An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the\n    use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org <a href="https://schema.org/docs/styleguide.html">style guide</a>.')
    alternate_name: Text | list[Text] | None = Field(default=None, alias='alternateName', description='An alias for the item.')
    description: Text | TextObject | list[Text | TextObject] | None = Field(default=None, alias='description', description='A description of the item.')
    disambiguating_description: Text | list[Text] | None = Field(default=None, alias='disambiguatingDescription', description='A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.')
    identifier: PropertyValue | Text | URL | list[PropertyValue | Text | URL] | None = Field(default=None, alias='identifier', description='The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.\n        ')
    image: ImageObject | URL | list[ImageObject | URL] | None = Field(default=None, alias='image', description='An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].')
    main_entity_of_page: CreativeWork | URL | list[CreativeWork | URL] | None = Field(default=None, alias='mainEntityOfPage', description='Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.\n\nInverse-property: `mainEntity`.')
    name: Text | list[Text] | None = Field(default=None, alias='name', description='The name of the item.')
    owner: Organization | Person | list[Organization | Person] | None = Field(default=None, alias='owner', description='A person or organization who owns this Thing.\n\nInverse-property: `owns`.')
    potential_action: Action | list[Action] | None = Field(default=None, alias='potentialAction', description="Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.")
    same_as: URL | list[URL] | None = Field(default=None, alias='sameAs', description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.")
    subject_of: CreativeWork | Event | list[CreativeWork | Event] | None = Field(default=None, alias='subjectOf', description='A CreativeWork or Event about this Thing.\n\nInverse-property: `about`.')
    url: URL | list[URL] | None = Field(default=None, alias='url', description='URL of the item.')
