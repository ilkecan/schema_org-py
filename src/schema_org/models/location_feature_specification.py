# Generated Python code is licensed under MIT.
# Schema.org descriptions are licensed under CC BY-SA 3.0.
# See LICENSE-SCHEMA-ORG.txt.

from __future__ import annotations

from typing import ClassVar, Literal

from schema_org.base import PropertyMetadata, SchemaModel, SchemaValue
from pydantic import Field
from schema_org.datatypes import Boolean
from schema_org.datatypes import Date
from schema_org.datatypes import DateTime
from schema_org.datatypes import Number
from schema_org.datatypes import Text
from schema_org.datatypes import URL
from schema_org.enums import ActionStatusType
from schema_org.enums import AdultOrientedEnumeration
from schema_org.enums import BedType
from schema_org.enums import BoardingPolicyType
from schema_org.enums import BodyMeasurementTypeEnumeration
from schema_org.enums import BookFormatType
from schema_org.enums import BusinessEntityType
from schema_org.enums import BusinessFunction
from schema_org.enums import CarUsageType
from schema_org.enums import CertificationStatusEnumeration
from schema_org.enums import ContactPointOption
from schema_org.enums import DENonprofitType
from schema_org.enums import DayOfWeek
from schema_org.enums import DeliveryMethod
from schema_org.enums import DigitalDocumentPermissionType
from schema_org.enums import DigitalPlatformEnumeration
from schema_org.enums import DriveWheelConfigurationValue
from schema_org.enums import DrugCostCategory
from schema_org.enums import DrugPregnancyCategory
from schema_org.enums import DrugPrescriptionStatus
from schema_org.enums import EUEnergyEfficiencyEnumeration
from schema_org.enums import EnergyEfficiencyEnumeration
from schema_org.enums import EnergyStarEnergyEfficiencyEnumeration
from schema_org.enums import Enumeration
from schema_org.enums import EventAttendanceModeEnumeration
from schema_org.enums import EventStatusType
from schema_org.enums import FulfillmentTypeEnumeration
from schema_org.enums import GameAvailabilityEnumeration
from schema_org.enums import GamePlayMode
from schema_org.enums import GameServerStatus
from schema_org.enums import GenderType
from schema_org.enums import GovernmentBenefitsType
from schema_org.enums import HealthAspectEnumeration
from schema_org.enums import IPTCDigitalSourceEnumeration
from schema_org.enums import ITNonprofitType
from schema_org.enums import IncentiveQualifiedExpenseType
from schema_org.enums import IncentiveStatus
from schema_org.enums import IncentiveType
from schema_org.enums import InfectiousAgentClass
from schema_org.enums import ItemAvailability
from schema_org.enums import ItemListOrderType
from schema_org.enums import LegalForceStatus
from schema_org.enums import LegalValueLevel
from schema_org.enums import MapCategoryType
from schema_org.enums import MeasurementMethodEnum
from schema_org.enums import MeasurementTypeEnumeration
from schema_org.enums import MediaEnumeration
from schema_org.enums import MediaManipulationRatingEnumeration
from schema_org.enums import MedicalAudienceType
from schema_org.enums import MedicalDevicePurpose
from schema_org.enums import MedicalEnumeration
from schema_org.enums import MedicalEvidenceLevel
from schema_org.enums import MedicalImagingTechnique
from schema_org.enums import MedicalObservationalStudyDesign
from schema_org.enums import MedicalProcedureType
from schema_org.enums import MedicalSpecialty
from schema_org.enums import MedicalStudyStatus
from schema_org.enums import MedicalTrialDesign
from schema_org.enums import MedicineSystem
from schema_org.enums import MerchantReturnEnumeration
from schema_org.enums import MusicAlbumProductionType
from schema_org.enums import MusicAlbumReleaseType
from schema_org.enums import MusicReleaseFormatType
from schema_org.enums import NLNonprofitType
from schema_org.enums import NonprofitType
from schema_org.enums import OfferItemCondition
from schema_org.enums import OrderStatus
from schema_org.enums import PaymentMethodType
from schema_org.enums import PaymentStatusType
from schema_org.enums import PhysicalActivityCategory
from schema_org.enums import PhysicalExam
from schema_org.enums import PriceComponentTypeEnumeration
from schema_org.enums import PriceTypeEnumeration
from schema_org.enums import ProductReturnEnumeration
from schema_org.enums import PurchaseType
from schema_org.enums import QualitativeValue
from schema_org.enums import RefundTypeEnumeration
from schema_org.enums import ReservationStatusType
from schema_org.enums import RestrictedDiet
from schema_org.enums import ReturnFeesEnumeration
from schema_org.enums import ReturnLabelSourceEnumeration
from schema_org.enums import ReturnMethodEnumeration
from schema_org.enums import RsvpResponseType
from schema_org.enums import SizeGroupEnumeration
from schema_org.enums import SizeSpecification
from schema_org.enums import SizeSystemEnumeration
from schema_org.enums import Specialty
from schema_org.enums import StatusEnumeration
from schema_org.enums import SteeringPositionValue
from schema_org.enums import TierBenefitEnumeration
from schema_org.enums import UKNonprofitType
from schema_org.enums import USNonprofitType
from schema_org.enums import WarrantyScope
from schema_org.enums import WearableMeasurementTypeEnumeration
from schema_org.enums import WearableSizeGroupEnumeration
from schema_org.enums import WearableSizeSystemEnumeration
from schema_org.models.property_value import PropertyValue

class LocationFeatureSpecification(PropertyValue):
    __doc__ = 'https://schema.org/LocationFeatureSpecification\n\nSpecifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.'
    SCHEMA_TYPE: ClassVar[str] = 'LocationFeatureSpecification'
    SCHEMA_TYPES: ClassVar[tuple[str, ...]] = ('LocationFeatureSpecification', 'PropertyValue', 'StructuredValue', 'Intangible', 'Thing')
    SCHEMA_PROPERTIES: ClassVar[tuple[PropertyMetadata, ...]] = (
        PropertyMetadata(name='additional_type', schema_name='additionalType', schema_url='https://schema.org/additionalType', ranges=('Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('http://www.w3.org/1999/02/22-rdf-syntax-ns#type',), domains=('Thing',), external_domains=(), comment='An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the\n    use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org <a href="https://schema.org/docs/styleguide.html">style guide</a>.', label='additionalType', contributors=(), sources=()),
        PropertyMetadata(name='alternate_name', schema_name='alternateName', schema_url='https://schema.org/alternateName', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='An alias for the item.', label='alternateName', contributors=(), sources=()),
        PropertyMetadata(name='description', schema_name='description', schema_url='https://schema.org/description', ranges=('Text', 'TextObject'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#description', 'http://purl.org/dc/terms/description', 'https://ref.gs1.org/voc/description'), subproperty_of=(), domains=('Thing',), external_domains=(), comment='A description of the item.', label='description', contributors=(), sources=()),
        PropertyMetadata(name='disambiguating_description', schema_name='disambiguatingDescription', schema_url='https://schema.org/disambiguatingDescription', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('description',), domains=('Thing',), external_domains=(), comment='A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.', label='disambiguatingDescription', contributors=(), sources=()),
        PropertyMetadata(name='hours_available', schema_name='hoursAvailable', schema_url='https://schema.org/hoursAvailable', ranges=('OpeningHoursSpecification',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('ContactPoint', 'LocationFeatureSpecification', 'Service'), external_domains=(), comment='The hours during which this service or contact is available.', label='hoursAvailable', contributors=(), sources=()),
        PropertyMetadata(name='identifier', schema_name='identifier', schema_url='https://schema.org/identifier', ranges=('PropertyValue', 'Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://purl.org/dc/terms/identifier', 'https://www.omg.org/spec/Commons/Identifiers/identifiedBy'), subproperty_of=(), domains=('Thing',), external_domains=(), comment='The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.\n        ', label='identifier', contributors=(), sources=()),
        PropertyMetadata(name='image', schema_name='image', schema_url='https://schema.org/image', ranges=('ImageObject', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#image',), subproperty_of=(), domains=('Thing',), external_domains=(), comment='An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].', label='image', contributors=(), sources=()),
        PropertyMetadata(name='main_entity_of_page', schema_name='mainEntityOfPage', schema_url='https://schema.org/mainEntityOfPage', ranges=('CreativeWork', 'URL'), external_ranges=(), inverse_of='mainEntity', superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.', label='mainEntityOfPage', contributors=(), sources=()),
        PropertyMetadata(name='max_value', schema_name='maxValue', schema_url='https://schema.org/maxValue', ranges=('Number',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('https://www.omg.org/spec/Commons/Quantities/hasUpperBound',), domains=('MonetaryAmount', 'PropertyValue', 'PropertyValueSpecification', 'QuantitativeValue'), external_domains=(), comment='The upper value of some characteristic or property.', label='maxValue', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
        PropertyMetadata(name='measurement_method', schema_name='measurementMethod', schema_url='https://schema.org/measurementMethod', ranges=('DefinedTerm', 'MeasurementMethodEnum', 'Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('measurementTechnique',), domains=('DataCatalog', 'DataDownload', 'Dataset', 'Observation', 'PropertyValue', 'StatisticalVariable'), external_domains=(), comment='A subproperty of [[measurementTechnique]] that can be used for specifying specific methods, in particular via [[MeasurementMethodEnum]].', label='measurementMethod', contributors=(), sources=('https://github.com/schemaorg/schemaorg/issues/1425',)),
        PropertyMetadata(name='measurement_technique', schema_name='measurementTechnique', schema_url='https://schema.org/measurementTechnique', ranges=('DefinedTerm', 'MeasurementMethodEnum', 'Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('DataCatalog', 'DataDownload', 'Dataset', 'Observation', 'PropertyValue', 'StatisticalVariable'), external_domains=(), comment='A technique, method or technology used in an [[Observation]], [[StatisticalVariable]] or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]]; for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each [[variableMeasured]] will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of [[variableMeasured]] called [[measuredProperty]] is applicable.\n    \nThe [[measurementTechnique]] property helps when extra clarification is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery. \n\nFor example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". \n\nIf there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]]. The value can also be from an enumeration, organized as a [[MeasurementMethodEnum]].', label='measurementTechnique', contributors=(), sources=('https://github.com/schemaorg/schemaorg/issues/1425',)),
        PropertyMetadata(name='min_value', schema_name='minValue', schema_url='https://schema.org/minValue', ranges=('Number',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=('https://www.omg.org/spec/Commons/Quantities/hasLowerBound',), domains=('MonetaryAmount', 'PropertyValue', 'PropertyValueSpecification', 'QuantitativeValue'), external_domains=(), comment='The lower value of some characteristic or property.', label='minValue', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
        PropertyMetadata(name='name', schema_name='name', schema_url='https://schema.org/name', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#title', 'http://purl.org/dc/terms/title', 'https://www.omg.org/spec/Commons/Text/hasName'), subproperty_of=('http://www.w3.org/2000/01/rdf-schema#label',), domains=('Thing',), external_domains=(), comment='The name of the item.', label='name', contributors=(), sources=()),
        PropertyMetadata(name='owner', schema_name='owner', schema_url='https://schema.org/owner', ranges=('Organization', 'Person'), external_ranges=(), inverse_of='owns', superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='A person or organization who owns this Thing.', label='owner', contributors=(), sources=('https://github.com/schemaorg/schemaorg/issues/4603',)),
        PropertyMetadata(name='potential_action', schema_name='potentialAction', schema_url='https://schema.org/potentialAction', ranges=('Action',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment="Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.", label='potentialAction', contributors=(), sources=()),
        PropertyMetadata(name='property_id', schema_name='propertyID', schema_url='https://schema.org/propertyID', ranges=('Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('PropertyValue',), external_domains=(), comment='A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be\n(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific ID of the property), or (3)\na URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).\nStandards bodies should promote a standard prefix for the identifiers of properties from their standards.', label='propertyID', contributors=(), sources=()),
        PropertyMetadata(name='same_as', schema_name='sameAs', schema_url='https://schema.org/sameAs', ranges=('URL',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.", label='sameAs', contributors=(), sources=()),
        PropertyMetadata(name='subject_of', schema_name='subjectOf', schema_url='https://schema.org/subjectOf', ranges=('CreativeWork', 'Event'), external_ranges=(), inverse_of='about', superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('Thing',), external_domains=(), comment='A CreativeWork or Event about this Thing.', label='subjectOf', contributors=(), sources=('https://github.com/schemaorg/schemaorg/issues/1670',)),
        PropertyMetadata(name='unit_code', schema_name='unitCode', schema_url='https://schema.org/unitCode', ranges=('Text', 'URL'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('PropertyValue', 'QuantitativeValue', 'TypeAndQuantityNode', 'UnitPriceSpecification'), external_domains=(), comment='The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.', label='unitCode', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
        PropertyMetadata(name='unit_text', schema_name='unitText', schema_url='https://schema.org/unitText', ranges=('Text',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('PropertyValue', 'QuantitativeValue', 'TypeAndQuantityNode', 'UnitPriceSpecification'), external_domains=(), comment="A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for\n<a href='unitCode'>unitCode</a>.", label='unitText', contributors=(), sources=()),
        PropertyMetadata(name='url', schema_name='url', schema_url='https://schema.org/url', ranges=('URL',), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('http://ogp.me/ns#url',), subproperty_of=(), domains=('Thing',), external_domains=(), comment='URL of the item.', label='url', contributors=(), sources=()),
        PropertyMetadata(name='valid_from', schema_name='validFrom', schema_url='https://schema.org/validFrom', ranges=('Date', 'DateTime'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate',), subproperty_of=(), domains=('Certification', 'Demand', 'FinancialIncentive', 'LocationFeatureSpecification', 'MonetaryAmount', 'Offer', 'OpeningHoursSpecification', 'Permit', 'PriceSpecification'), external_domains=(), comment='The date when the item becomes valid.', label='validFrom', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
        PropertyMetadata(name='valid_through', schema_name='validThrough', schema_url='https://schema.org/validThrough', ranges=('Date', 'DateTime'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=('https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate',), subproperty_of=(), domains=('Demand', 'FinancialIncentive', 'JobPosting', 'LocationFeatureSpecification', 'MonetaryAmount', 'Offer', 'OpeningHoursSpecification', 'PriceSpecification'), external_domains=(), comment='The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.', label='validThrough', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
        PropertyMetadata(name='value', schema_name='value', schema_url='https://schema.org/value', ranges=('Boolean', 'Number', 'StructuredValue', 'Text'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('MonetaryAmount', 'PropertyValue', 'QuantitativeValue'), external_domains=(), comment="The value of a [[QuantitativeValue]] (including [[Observation]]) or property value node.\\n\\n* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.\\n* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.\\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.", label='value', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
        PropertyMetadata(name='value_reference', schema_name='valueReference', schema_url='https://schema.org/valueReference', ranges=('DefinedTerm', 'Enumeration', 'MeasurementTypeEnumeration', 'PropertyValue', 'QualitativeValue', 'QuantitativeValue', 'StructuredValue', 'Text'), external_ranges=(), inverse_of=None, superseded_by=None, supersedes=(), equivalent_properties=(), subproperty_of=(), domains=('PropertyValue', 'QualitativeValue', 'QuantitativeValue'), external_domains=(), comment='A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.', label='valueReference', contributors=('https://schema.org/docs/collab/GoodRelationsTerms',), sources=()),
    )
    schema_id: str | None = Field(default=None, alias='@id')
    schema_type: Literal['LocationFeatureSpecification'] = Field(default='LocationFeatureSpecification', alias='@type', frozen=True)
    hours_available: OpeningHoursSpecification | list[OpeningHoursSpecification] | None = Field(default=None, alias='hoursAvailable', description='The hours during which this service or contact is available.')
    valid_from: Date | DateTime | list[Date | DateTime] | None = Field(default=None, alias='validFrom', description='The date when the item becomes valid.')
    valid_through: Date | DateTime | list[Date | DateTime] | None = Field(default=None, alias='validThrough', description='The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.')
