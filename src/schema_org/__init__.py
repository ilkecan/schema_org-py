# Generated Python code is licensed under MIT.
# Schema.org descriptions are licensed under CC BY-SA 3.0.
# See LICENSE-SCHEMA-ORG.txt.

from importlib import import_module
from typing import TYPE_CHECKING

from .base import CircularReferenceError, ClassMetadata, EnumerationMemberMetadata, JsonValue, PropertyMetadata, SchemaEnum, SchemaMap, SchemaModel, SchemaScalar, SchemaValue
from .schema_version import SCHEMA_VERSION

if TYPE_CHECKING:
    from .models.three_d_model import ThreeDModel
    from .models.am_radio_channel import AMRadioChannel
    from .models.api_reference import APIReference
    from .models.about_page import AboutPage
    from .models.accept_action import AcceptAction
    from .models.accommodation import Accommodation
    from .models.accounting_service import AccountingService
    from .models.achieve_action import AchieveAction
    from .models.action import Action
    from .models.action_access_specification import ActionAccessSpecification
    from .models.activate_action import ActivateAction
    from .models.add_action import AddAction
    from .models.administrative_area import AdministrativeArea
    from .models.adult_entertainment import AdultEntertainment
    from .models.advertiser_content_article import AdvertiserContentArticle
    from .models.aggregate_offer import AggregateOffer
    from .models.aggregate_rating import AggregateRating
    from .models.agree_action import AgreeAction
    from .models.airline import Airline
    from .models.airport import Airport
    from .models.alignment_object import AlignmentObject
    from .models.allocate_action import AllocateAction
    from .models.amp_story import AmpStory
    from .models.amusement_park import AmusementPark
    from .models.analysis_news_article import AnalysisNewsArticle
    from .models.anatomical_structure import AnatomicalStructure
    from .models.anatomical_system import AnatomicalSystem
    from .models.animal_shelter import AnimalShelter
    from .models.answer import Answer
    from .models.apartment import Apartment
    from .models.apartment_complex import ApartmentComplex
    from .models.append_action import AppendAction
    from .models.apply_action import ApplyAction
    from .models.approved_indication import ApprovedIndication
    from .models.aquarium import Aquarium
    from .models.archive_component import ArchiveComponent
    from .models.archive_organization import ArchiveOrganization
    from .models.arrive_action import ArriveAction
    from .models.art_gallery import ArtGallery
    from .models.artery import Artery
    from .models.article import Article
    from .models.ask_action import AskAction
    from .models.ask_public_news_article import AskPublicNewsArticle
    from .models.assess_action import AssessAction
    from .models.assign_action import AssignAction
    from .models.atlas import Atlas
    from .models.attorney import Attorney
    from .models.audience import Audience
    from .models.audio_object import AudioObject
    from .models.audio_object_snapshot import AudioObjectSnapshot
    from .models.audiobook import Audiobook
    from .models.authenticate_action import AuthenticateAction
    from .models.authorize_action import AuthorizeAction
    from .models.auto_body_shop import AutoBodyShop
    from .models.auto_dealer import AutoDealer
    from .models.auto_parts_store import AutoPartsStore
    from .models.auto_rental import AutoRental
    from .models.auto_repair import AutoRepair
    from .models.auto_wash import AutoWash
    from .models.automated_teller import AutomatedTeller
    from .models.automotive_business import AutomotiveBusiness
    from .models.background_news_article import BackgroundNewsArticle
    from .models.bakery import Bakery
    from .models.bank_account import BankAccount
    from .models.bank_or_credit_union import BankOrCreditUnion
    from .models.bar_or_pub import BarOrPub
    from .models.barcode import Barcode
    from .models.beach import Beach
    from .models.beauty_salon import BeautySalon
    from .models.bed_and_breakfast import BedAndBreakfast
    from .models.bed_details import BedDetails
    from .models.befriend_action import BefriendAction
    from .models.bike_store import BikeStore
    from .models.bio_chem_entity import BioChemEntity
    from .models.blog import Blog
    from .models.blog_posting import BlogPosting
    from .models.blood_test import BloodTest
    from .models.boat_reservation import BoatReservation
    from .models.boat_terminal import BoatTerminal
    from .models.boat_trip import BoatTrip
    from .models.body_of_water import BodyOfWater
    from .models.bone import Bone
    from .models.book import Book
    from .models.book_series import BookSeries
    from .models.book_store import BookStore
    from .models.bookmark_action import BookmarkAction
    from .models.borrow_action import BorrowAction
    from .models.bowling_alley import BowlingAlley
    from .models.brain_structure import BrainStructure
    from .models.brand import Brand
    from .models.breadcrumb_list import BreadcrumbList
    from .models.brewery import Brewery
    from .models.bridge import Bridge
    from .models.broadcast_channel import BroadcastChannel
    from .models.broadcast_event import BroadcastEvent
    from .models.broadcast_frequency_specification import BroadcastFrequencySpecification
    from .models.broadcast_service import BroadcastService
    from .models.brokerage_account import BrokerageAccount
    from .models.buddhist_temple import BuddhistTemple
    from .models.bus_or_coach import BusOrCoach
    from .models.bus_reservation import BusReservation
    from .models.bus_station import BusStation
    from .models.bus_stop import BusStop
    from .models.bus_trip import BusTrip
    from .models.business_audience import BusinessAudience
    from .models.business_event import BusinessEvent
    from .models.buy_action import BuyAction
    from .models.cdcpmd_record import CDCPMDRecord
    from .models.cable_or_satellite_service import CableOrSatelliteService
    from .models.cafe_or_coffee_shop import CafeOrCoffeeShop
    from .models.campground import Campground
    from .models.camping_pitch import CampingPitch
    from .models.canal import Canal
    from .models.cancel_action import CancelAction
    from .models.car import Car
    from .models.casino import Casino
    from .models.category_code import CategoryCode
    from .models.category_code_set import CategoryCodeSet
    from .models.catholic_church import CatholicChurch
    from .models.cemetery import Cemetery
    from .models.certification import Certification
    from .models.chapter import Chapter
    from .models.check_action import CheckAction
    from .models.check_in_action import CheckInAction
    from .models.check_out_action import CheckOutAction
    from .models.checkout_page import CheckoutPage
    from .models.chemical_substance import ChemicalSubstance
    from .models.child_care import ChildCare
    from .models.childrens_event import ChildrensEvent
    from .models.choose_action import ChooseAction
    from .models.church import Church
    from .models.city import City
    from .models.city_hall import CityHall
    from .models.civic_structure import CivicStructure
    from .models.claim import Claim
    from .models.claim_review import ClaimReview
    from .models.class_ import Class
    from .models.clip import Clip
    from .models.clothing_store import ClothingStore
    from .models.code import Code
    from .models.collection import Collection
    from .models.collection_page import CollectionPage
    from .models.college_or_university import CollegeOrUniversity
    from .models.comedy_club import ComedyClub
    from .models.comedy_event import ComedyEvent
    from .models.comic_cover_art import ComicCoverArt
    from .models.comic_issue import ComicIssue
    from .models.comic_series import ComicSeries
    from .models.comic_story import ComicStory
    from .models.comment import Comment
    from .models.comment_action import CommentAction
    from .models.communicate_action import CommunicateAction
    from .models.complete_data_feed import CompleteDataFeed
    from .models.compound_price_specification import CompoundPriceSpecification
    from .models.computer_language import ComputerLanguage
    from .models.computer_store import ComputerStore
    from .models.conference_event import ConferenceEvent
    from .models.confirm_action import ConfirmAction
    from .models.consortium import Consortium
    from .models.constraint_node import ConstraintNode
    from .models.consume_action import ConsumeAction
    from .models.contact_page import ContactPage
    from .models.contact_point import ContactPoint
    from .models.continent import Continent
    from .models.control_action import ControlAction
    from .models.convenience_store import ConvenienceStore
    from .models.conversation import Conversation
    from .models.cook_action import CookAction
    from .models.cooperative import Cooperative
    from .models.corporation import Corporation
    from .models.correction_comment import CorrectionComment
    from .models.country import Country
    from .models.course import Course
    from .models.course_instance import CourseInstance
    from .models.courthouse import Courthouse
    from .models.cover_art import CoverArt
    from .models.covid_testing_facility import CovidTestingFacility
    from .models.create_action import CreateAction
    from .models.creative_work import CreativeWork
    from .models.creative_work_season import CreativeWorkSeason
    from .models.creative_work_series import CreativeWorkSeries
    from .models.credential import Credential
    from .models.credit_card import CreditCard
    from .models.crematorium import Crematorium
    from .models.critic_review import CriticReview
    from .models.currency_conversion_service import CurrencyConversionService
    from .models.d_dx_element import DDxElement
    from .models.dance_event import DanceEvent
    from .models.dance_group import DanceGroup
    from .models.data_catalog import DataCatalog
    from .models.data_download import DataDownload
    from .models.data_feed import DataFeed
    from .models.data_feed_item import DataFeedItem
    from .models.dataset import Dataset
    from .models.dated_money_specification import DatedMoneySpecification
    from .models.day_spa import DaySpa
    from .models.deactivate_action import DeactivateAction
    from .models.defence_establishment import DefenceEstablishment
    from .models.defined_region import DefinedRegion
    from .models.defined_term import DefinedTerm
    from .models.defined_term_set import DefinedTermSet
    from .models.delete_action import DeleteAction
    from .models.delivery_charge_specification import DeliveryChargeSpecification
    from .models.delivery_event import DeliveryEvent
    from .models.delivery_time_settings import DeliveryTimeSettings
    from .models.demand import Demand
    from .models.dentist import Dentist
    from .models.depart_action import DepartAction
    from .models.department_store import DepartmentStore
    from .models.deposit_account import DepositAccount
    from .models.diagnostic_lab import DiagnosticLab
    from .models.diagnostic_procedure import DiagnosticProcedure
    from .models.diet import Diet
    from .models.dietary_supplement import DietarySupplement
    from .models.digital_document import DigitalDocument
    from .models.digital_document_permission import DigitalDocumentPermission
    from .models.disagree_action import DisagreeAction
    from .models.discover_action import DiscoverAction
    from .models.discussion_forum_posting import DiscussionForumPosting
    from .models.dislike_action import DislikeAction
    from .models.distillery import Distillery
    from .models.donate_action import DonateAction
    from .models.dose_schedule import DoseSchedule
    from .models.download_action import DownloadAction
    from .models.draw_action import DrawAction
    from .models.drawing import Drawing
    from .models.drink_action import DrinkAction
    from .models.drug import Drug
    from .models.drug_class import DrugClass
    from .models.drug_cost import DrugCost
    from .models.drug_legal_status import DrugLegalStatus
    from .models.drug_strength import DrugStrength
    from .models.dry_cleaning_or_laundry import DryCleaningOrLaundry
    from .models.eat_action import EatAction
    from .models.education_event import EducationEvent
    from .models.educational_audience import EducationalAudience
    from .models.educational_occupational_credential import EducationalOccupationalCredential
    from .models.educational_occupational_program import EducationalOccupationalProgram
    from .models.educational_organization import EducationalOrganization
    from .models.electrician import Electrician
    from .models.electronics_store import ElectronicsStore
    from .models.elementary_school import ElementarySchool
    from .models.email_message import EmailMessage
    from .models.embassy import Embassy
    from .models.emergency_service import EmergencyService
    from .models.employee_role import EmployeeRole
    from .models.employer_aggregate_rating import EmployerAggregateRating
    from .models.employer_review import EmployerReview
    from .models.employment_agency import EmploymentAgency
    from .models.endorse_action import EndorseAction
    from .models.endorsement_rating import EndorsementRating
    from .models.energy_consumption_details import EnergyConsumptionDetails
    from .models.engine_specification import EngineSpecification
    from .models.entertainment_business import EntertainmentBusiness
    from .models.entry_point import EntryPoint
    from .models.episode import Episode
    from .models.error import Error
    from .models.event import Event
    from .models.event_reservation import EventReservation
    from .models.event_series import EventSeries
    from .models.event_venue import EventVenue
    from .models.exchange_rate_specification import ExchangeRateSpecification
    from .models.exercise_action import ExerciseAction
    from .models.exercise_gym import ExerciseGym
    from .models.exercise_plan import ExercisePlan
    from .models.exhibition_event import ExhibitionEvent
    from .models.faq_page import FAQPage
    from .models.fm_radio_channel import FMRadioChannel
    from .models.fast_food_restaurant import FastFoodRestaurant
    from .models.festival import Festival
    from .models.film_action import FilmAction
    from .models.financial_incentive import FinancialIncentive
    from .models.financial_product import FinancialProduct
    from .models.financial_service import FinancialService
    from .models.find_action import FindAction
    from .models.fire_station import FireStation
    from .models.flight import Flight
    from .models.flight_reservation import FlightReservation
    from .models.floor_plan import FloorPlan
    from .models.florist import Florist
    from .models.follow_action import FollowAction
    from .models.food_establishment import FoodEstablishment
    from .models.food_establishment_reservation import FoodEstablishmentReservation
    from .models.food_event import FoodEvent
    from .models.food_service import FoodService
    from .models.funding_agency import FundingAgency
    from .models.funding_scheme import FundingScheme
    from .models.furniture_store import FurnitureStore
    from .models.game import Game
    from .models.game_server import GameServer
    from .models.garden_store import GardenStore
    from .models.gas_station import GasStation
    from .models.gated_residence_community import GatedResidenceCommunity
    from .models.gene import Gene
    from .models.general_contractor import GeneralContractor
    from .models.geo_circle import GeoCircle
    from .models.geo_coordinates import GeoCoordinates
    from .models.geo_shape import GeoShape
    from .models.geospatial_geometry import GeospatialGeometry
    from .models.give_action import GiveAction
    from .models.golf_course import GolfCourse
    from .models.government_building import GovernmentBuilding
    from .models.government_office import GovernmentOffice
    from .models.government_organization import GovernmentOrganization
    from .models.government_permit import GovernmentPermit
    from .models.government_service import GovernmentService
    from .models.grant import Grant
    from .models.grocery_store import GroceryStore
    from .models.guide import Guide
    from .models.hvac_business import HVACBusiness
    from .models.hackathon import Hackathon
    from .models.hair_salon import HairSalon
    from .models.hardware_store import HardwareStore
    from .models.health_and_beauty_business import HealthAndBeautyBusiness
    from .models.health_club import HealthClub
    from .models.health_insurance_plan import HealthInsurancePlan
    from .models.health_plan_cost_sharing_specification import HealthPlanCostSharingSpecification
    from .models.health_plan_formulary import HealthPlanFormulary
    from .models.health_plan_network import HealthPlanNetwork
    from .models.health_topic_content import HealthTopicContent
    from .models.high_school import HighSchool
    from .models.hindu_temple import HinduTemple
    from .models.hobby_shop import HobbyShop
    from .models.home_and_construction_business import HomeAndConstructionBusiness
    from .models.home_goods_store import HomeGoodsStore
    from .models.hospital import Hospital
    from .models.hostel import Hostel
    from .models.hotel import Hotel
    from .models.hotel_room import HotelRoom
    from .models.house import House
    from .models.house_painter import HousePainter
    from .models.how_to import HowTo
    from .models.how_to_direction import HowToDirection
    from .models.how_to_item import HowToItem
    from .models.how_to_section import HowToSection
    from .models.how_to_step import HowToStep
    from .models.how_to_supply import HowToSupply
    from .models.how_to_tip import HowToTip
    from .models.how_to_tool import HowToTool
    from .models.hyper_toc import HyperToc
    from .models.hyper_toc_entry import HyperTocEntry
    from .models.ice_cream_shop import IceCreamShop
    from .models.ignore_action import IgnoreAction
    from .models.image_gallery import ImageGallery
    from .models.image_object import ImageObject
    from .models.image_object_snapshot import ImageObjectSnapshot
    from .models.imaging_test import ImagingTest
    from .models.individual_physician import IndividualPhysician
    from .models.individual_product import IndividualProduct
    from .models.infectious_disease import InfectiousDisease
    from .models.inform_action import InformAction
    from .models.insert_action import InsertAction
    from .models.install_action import InstallAction
    from .models.instantaneous_event import InstantaneousEvent
    from .models.insurance_agency import InsuranceAgency
    from .models.intangible import Intangible
    from .models.interact_action import InteractAction
    from .models.interaction_counter import InteractionCounter
    from .models.internet_cafe import InternetCafe
    from .models.investment_fund import InvestmentFund
    from .models.investment_or_deposit import InvestmentOrDeposit
    from .models.invite_action import InviteAction
    from .models.invoice import Invoice
    from .models.item_list import ItemList
    from .models.item_page import ItemPage
    from .models.jewelry_store import JewelryStore
    from .models.job_posting import JobPosting
    from .models.join_action import JoinAction
    from .models.joint import Joint
    from .models.lake_body_of_water import LakeBodyOfWater
    from .models.landform import Landform
    from .models.landmarks_or_historical_buildings import LandmarksOrHistoricalBuildings
    from .models.language import Language
    from .models.learning_resource import LearningResource
    from .models.leave_action import LeaveAction
    from .models.legal_service import LegalService
    from .models.legislation import Legislation
    from .models.legislation_object import LegislationObject
    from .models.legislative_building import LegislativeBuilding
    from .models.lend_action import LendAction
    from .models.library import Library
    from .models.library_system import LibrarySystem
    from .models.lifestyle_modification import LifestyleModification
    from .models.ligament import Ligament
    from .models.like_action import LikeAction
    from .models.link_role import LinkRole
    from .models.liquor_store import LiquorStore
    from .models.list_item import ListItem
    from .models.listen_action import ListenAction
    from .models.literary_event import LiteraryEvent
    from .models.live_blog_posting import LiveBlogPosting
    from .models.loan_or_credit import LoanOrCredit
    from .models.local_business import LocalBusiness
    from .models.location_feature_specification import LocationFeatureSpecification
    from .models.locksmith import Locksmith
    from .models.lodging_business import LodgingBusiness
    from .models.lodging_reservation import LodgingReservation
    from .models.login_action import LoginAction
    from .models.lose_action import LoseAction
    from .models.lymphatic_vessel import LymphaticVessel
    from .models.manuscript import Manuscript
    from .models.map import Map
    from .models.marry_action import MarryAction
    from .models.math_solver import MathSolver
    from .models.maximum_dose_schedule import MaximumDoseSchedule
    from .models.media_gallery import MediaGallery
    from .models.media_object import MediaObject
    from .models.media_review import MediaReview
    from .models.media_review_item import MediaReviewItem
    from .models.media_subscription import MediaSubscription
    from .models.medical_audience import MedicalAudience
    from .models.medical_business import MedicalBusiness
    from .models.medical_cause import MedicalCause
    from .models.medical_clinic import MedicalClinic
    from .models.medical_code import MedicalCode
    from .models.medical_condition import MedicalCondition
    from .models.medical_condition_stage import MedicalConditionStage
    from .models.medical_contraindication import MedicalContraindication
    from .models.medical_device import MedicalDevice
    from .models.medical_entity import MedicalEntity
    from .models.medical_guideline import MedicalGuideline
    from .models.medical_guideline_contraindication import MedicalGuidelineContraindication
    from .models.medical_guideline_recommendation import MedicalGuidelineRecommendation
    from .models.medical_indication import MedicalIndication
    from .models.medical_intangible import MedicalIntangible
    from .models.medical_observational_study import MedicalObservationalStudy
    from .models.medical_organization import MedicalOrganization
    from .models.medical_procedure import MedicalProcedure
    from .models.medical_risk_calculator import MedicalRiskCalculator
    from .models.medical_risk_estimator import MedicalRiskEstimator
    from .models.medical_risk_factor import MedicalRiskFactor
    from .models.medical_risk_score import MedicalRiskScore
    from .models.medical_scholarly_article import MedicalScholarlyArticle
    from .models.medical_sign import MedicalSign
    from .models.medical_sign_or_symptom import MedicalSignOrSymptom
    from .models.medical_study import MedicalStudy
    from .models.medical_symptom import MedicalSymptom
    from .models.medical_test import MedicalTest
    from .models.medical_test_panel import MedicalTestPanel
    from .models.medical_therapy import MedicalTherapy
    from .models.medical_trial import MedicalTrial
    from .models.medical_web_page import MedicalWebPage
    from .models.meeting_room import MeetingRoom
    from .models.member_program import MemberProgram
    from .models.member_program_tier import MemberProgramTier
    from .models.mens_clothing_store import MensClothingStore
    from .models.menu import Menu
    from .models.menu_item import MenuItem
    from .models.menu_section import MenuSection
    from .models.merchant_return_policy import MerchantReturnPolicy
    from .models.merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .models.message import Message
    from .models.middle_school import MiddleSchool
    from .models.mobile_application import MobileApplication
    from .models.mobile_phone_store import MobilePhoneStore
    from .models.molecular_entity import MolecularEntity
    from .models.monetary_amount import MonetaryAmount
    from .models.monetary_amount_distribution import MonetaryAmountDistribution
    from .models.monetary_grant import MonetaryGrant
    from .models.money_transfer import MoneyTransfer
    from .models.mortgage_loan import MortgageLoan
    from .models.mosque import Mosque
    from .models.motel import Motel
    from .models.motorcycle import Motorcycle
    from .models.motorcycle_dealer import MotorcycleDealer
    from .models.motorcycle_repair import MotorcycleRepair
    from .models.motorized_bicycle import MotorizedBicycle
    from .models.mountain import Mountain
    from .models.move_action import MoveAction
    from .models.movie import Movie
    from .models.movie_clip import MovieClip
    from .models.movie_rental_store import MovieRentalStore
    from .models.movie_series import MovieSeries
    from .models.movie_theater import MovieTheater
    from .models.moving_company import MovingCompany
    from .models.muscle import Muscle
    from .models.museum import Museum
    from .models.music_album import MusicAlbum
    from .models.music_composition import MusicComposition
    from .models.music_event import MusicEvent
    from .models.music_group import MusicGroup
    from .models.music_playlist import MusicPlaylist
    from .models.music_recording import MusicRecording
    from .models.music_release import MusicRelease
    from .models.music_store import MusicStore
    from .models.music_venue import MusicVenue
    from .models.music_video_object import MusicVideoObject
    from .models.ngo import NGO
    from .models.nail_salon import NailSalon
    from .models.nerve import Nerve
    from .models.news_article import NewsArticle
    from .models.news_media_organization import NewsMediaOrganization
    from .models.newspaper import Newspaper
    from .models.night_club import NightClub
    from .models.notary import Notary
    from .models.note_digital_document import NoteDigitalDocument
    from .models.nutrition_information import NutritionInformation
    from .models.observation import Observation
    from .models.occupation import Occupation
    from .models.occupational_experience_requirements import OccupationalExperienceRequirements
    from .models.occupational_therapy import OccupationalTherapy
    from .models.ocean_body_of_water import OceanBodyOfWater
    from .models.offer import Offer
    from .models.offer_catalog import OfferCatalog
    from .models.offer_for_lease import OfferForLease
    from .models.offer_for_purchase import OfferForPurchase
    from .models.offer_shipping_details import OfferShippingDetails
    from .models.office_equipment_store import OfficeEquipmentStore
    from .models.on_demand_event import OnDemandEvent
    from .models.online_business import OnlineBusiness
    from .models.online_marketplace import OnlineMarketplace
    from .models.online_store import OnlineStore
    from .models.opening_hours_specification import OpeningHoursSpecification
    from .models.operating_system import OperatingSystem
    from .models.opinion_news_article import OpinionNewsArticle
    from .models.optician import Optician
    from .models.order import Order
    from .models.order_action import OrderAction
    from .models.order_item import OrderItem
    from .models.organization import Organization
    from .models.organization_role import OrganizationRole
    from .models.organize_action import OrganizeAction
    from .models.outlet_store import OutletStore
    from .models.ownership_info import OwnershipInfo
    from .models.paint_action import PaintAction
    from .models.painting import Painting
    from .models.palliative_procedure import PalliativeProcedure
    from .models.parcel_delivery import ParcelDelivery
    from .models.parent_audience import ParentAudience
    from .models.park import Park
    from .models.parking_facility import ParkingFacility
    from .models.pathology_test import PathologyTest
    from .models.patient import Patient
    from .models.pawn_shop import PawnShop
    from .models.pay_action import PayAction
    from .models.payment_card import PaymentCard
    from .models.payment_charge_specification import PaymentChargeSpecification
    from .models.payment_method import PaymentMethod
    from .models.payment_service import PaymentService
    from .models.people_audience import PeopleAudience
    from .models.perform_action import PerformAction
    from .models.performance_role import PerformanceRole
    from .models.performing_arts_event import PerformingArtsEvent
    from .models.performing_arts_theater import PerformingArtsTheater
    from .models.performing_group import PerformingGroup
    from .models.periodical import Periodical
    from .models.permit import Permit
    from .models.person import Person
    from .models.pet_store import PetStore
    from .models.pharmacy import Pharmacy
    from .models.photograph import Photograph
    from .models.photograph_action import PhotographAction
    from .models.physical_activity import PhysicalActivity
    from .models.physical_therapy import PhysicalTherapy
    from .models.physician import Physician
    from .models.physicians_office import PhysiciansOffice
    from .models.place import Place
    from .models.place_of_worship import PlaceOfWorship
    from .models.plan_action import PlanAction
    from .models.play import Play
    from .models.play_action import PlayAction
    from .models.play_game_action import PlayGameAction
    from .models.playground import Playground
    from .models.plumber import Plumber
    from .models.podcast_episode import PodcastEpisode
    from .models.podcast_season import PodcastSeason
    from .models.podcast_series import PodcastSeries
    from .models.police_station import PoliceStation
    from .models.political_party import PoliticalParty
    from .models.pond import Pond
    from .models.post_office import PostOffice
    from .models.postal_address import PostalAddress
    from .models.postal_code_range_specification import PostalCodeRangeSpecification
    from .models.poster import Poster
    from .models.pre_order_action import PreOrderAction
    from .models.prepend_action import PrependAction
    from .models.preschool import Preschool
    from .models.presentation_digital_document import PresentationDigitalDocument
    from .models.prevention_indication import PreventionIndication
    from .models.price_specification import PriceSpecification
    from .models.product import Product
    from .models.product_collection import ProductCollection
    from .models.product_group import ProductGroup
    from .models.product_model import ProductModel
    from .models.product_return_policy import ProductReturnPolicy
    from .models.professional_service import ProfessionalService
    from .models.profile_page import ProfilePage
    from .models.program_membership import ProgramMembership
    from .models.project import Project
    from .models.property import Property
    from .models.property_value import PropertyValue
    from .models.property_value_specification import PropertyValueSpecification
    from .models.protein import Protein
    from .models.psychological_treatment import PsychologicalTreatment
    from .models.public_swimming_pool import PublicSwimmingPool
    from .models.public_toilet import PublicToilet
    from .models.publication_event import PublicationEvent
    from .models.publication_issue import PublicationIssue
    from .models.publication_volume import PublicationVolume
    from .models.qa_page import QAPage
    from .models.quantitative_value import QuantitativeValue
    from .models.quantitative_value_distribution import QuantitativeValueDistribution
    from .models.question import Question
    from .models.quiz import Quiz
    from .models.quotation import Quotation
    from .models.quote_action import QuoteAction
    from .models.rv_park import RVPark
    from .models.radiation_therapy import RadiationTherapy
    from .models.radio_broadcast_service import RadioBroadcastService
    from .models.radio_channel import RadioChannel
    from .models.radio_clip import RadioClip
    from .models.radio_episode import RadioEpisode
    from .models.radio_season import RadioSeason
    from .models.radio_series import RadioSeries
    from .models.radio_station import RadioStation
    from .models.rating import Rating
    from .models.react_action import ReactAction
    from .models.read_action import ReadAction
    from .models.real_estate_agent import RealEstateAgent
    from .models.real_estate_listing import RealEstateListing
    from .models.receive_action import ReceiveAction
    from .models.recipe import Recipe
    from .models.recommendation import Recommendation
    from .models.recommended_dose_schedule import RecommendedDoseSchedule
    from .models.recycling_center import RecyclingCenter
    from .models.register_action import RegisterAction
    from .models.reject_action import RejectAction
    from .models.rent_action import RentAction
    from .models.rental_car_reservation import RentalCarReservation
    from .models.repayment_specification import RepaymentSpecification
    from .models.replace_action import ReplaceAction
    from .models.reply_action import ReplyAction
    from .models.report import Report
    from .models.reportage_news_article import ReportageNewsArticle
    from .models.reported_dose_schedule import ReportedDoseSchedule
    from .models.research_organization import ResearchOrganization
    from .models.research_project import ResearchProject
    from .models.researcher import Researcher
    from .models.reservation import Reservation
    from .models.reservation_package import ReservationPackage
    from .models.reserve_action import ReserveAction
    from .models.reservoir import Reservoir
    from .models.reset_password_action import ResetPasswordAction
    from .models.residence import Residence
    from .models.resort import Resort
    from .models.restaurant import Restaurant
    from .models.resume_action import ResumeAction
    from .models.return_action import ReturnAction
    from .models.review import Review
    from .models.review_action import ReviewAction
    from .models.review_news_article import ReviewNewsArticle
    from .models.river_body_of_water import RiverBodyOfWater
    from .models.role import Role
    from .models.roofing_contractor import RoofingContractor
    from .models.room import Room
    from .models.rsvp_action import RsvpAction
    from .models.runtime_platform import RuntimePlatform
    from .models.sale_event import SaleEvent
    from .models.satirical_article import SatiricalArticle
    from .models.schedule import Schedule
    from .models.schedule_action import ScheduleAction
    from .models.scholarly_article import ScholarlyArticle
    from .models.school import School
    from .models.school_district import SchoolDistrict
    from .models.screening_event import ScreeningEvent
    from .models.sculpture import Sculpture
    from .models.sea_body_of_water import SeaBodyOfWater
    from .models.search_action import SearchAction
    from .models.search_rescue_organization import SearchRescueOrganization
    from .models.search_results_page import SearchResultsPage
    from .models.season import Season
    from .models.seat import Seat
    from .models.seek_to_action import SeekToAction
    from .models.self_storage import SelfStorage
    from .models.sell_action import SellAction
    from .models.send_action import SendAction
    from .models.sequential_art import SequentialArt
    from .models.series import Series
    from .models.service import Service
    from .models.service_channel import ServiceChannel
    from .models.service_period import ServicePeriod
    from .models.share_action import ShareAction
    from .models.sheet_music import SheetMusic
    from .models.shipping_conditions import ShippingConditions
    from .models.shipping_delivery_time import ShippingDeliveryTime
    from .models.shipping_rate_settings import ShippingRateSettings
    from .models.shipping_service import ShippingService
    from .models.shoe_store import ShoeStore
    from .models.shopping_center import ShoppingCenter
    from .models.short_story import ShortStory
    from .models.single_family_residence import SingleFamilyResidence
    from .models.site_navigation_element import SiteNavigationElement
    from .models.ski_resort import SkiResort
    from .models.social_event import SocialEvent
    from .models.social_media_posting import SocialMediaPosting
    from .models.software_application import SoftwareApplication
    from .models.software_source_code import SoftwareSourceCode
    from .models.solve_math_action import SolveMathAction
    from .models.some_products import SomeProducts
    from .models.speakable_specification import SpeakableSpecification
    from .models.special_announcement import SpecialAnnouncement
    from .models.sporting_goods_store import SportingGoodsStore
    from .models.sports_activity_location import SportsActivityLocation
    from .models.sports_club import SportsClub
    from .models.sports_event import SportsEvent
    from .models.sports_organization import SportsOrganization
    from .models.sports_team import SportsTeam
    from .models.spreadsheet_digital_document import SpreadsheetDigitalDocument
    from .models.stadium_or_arena import StadiumOrArena
    from .models.state import State
    from .models.statement import Statement
    from .models.statistical_population import StatisticalPopulation
    from .models.statistical_variable import StatisticalVariable
    from .models.store import Store
    from .models.structured_value import StructuredValue
    from .models.stupid_type import StupidType
    from .models.subscribe_action import SubscribeAction
    from .models.substance import Substance
    from .models.subway_station import SubwayStation
    from .models.suite import Suite
    from .models.superficial_anatomy import SuperficialAnatomy
    from .models.surgical_procedure import SurgicalProcedure
    from .models.suspend_action import SuspendAction
    from .models.syllabus import Syllabus
    from .models.synagogue import Synagogue
    from .models.tv_clip import TVClip
    from .models.tv_episode import TVEpisode
    from .models.tv_season import TVSeason
    from .models.tv_series import TVSeries
    from .models.table import Table
    from .models.take_action import TakeAction
    from .models.tattoo_parlor import TattooParlor
    from .models.taxi import Taxi
    from .models.taxi_reservation import TaxiReservation
    from .models.taxi_service import TaxiService
    from .models.taxi_stand import TaxiStand
    from .models.taxon import Taxon
    from .models.tech_article import TechArticle
    from .models.television_channel import TelevisionChannel
    from .models.television_station import TelevisionStation
    from .models.tennis_complex import TennisComplex
    from .models.text_digital_document import TextDigitalDocument
    from .models.text_object import TextObject
    from .models.theater_event import TheaterEvent
    from .models.theater_group import TheaterGroup
    from .models.therapeutic_procedure import TherapeuticProcedure
    from .models.thesis import Thesis
    from .models.thing import Thing
    from .models.ticket import Ticket
    from .models.tie_action import TieAction
    from .models.tip_action import TipAction
    from .models.tire_shop import TireShop
    from .models.tourist_attraction import TouristAttraction
    from .models.tourist_destination import TouristDestination
    from .models.tourist_information_center import TouristInformationCenter
    from .models.tourist_trip import TouristTrip
    from .models.toy_store import ToyStore
    from .models.track_action import TrackAction
    from .models.trade_action import TradeAction
    from .models.train_reservation import TrainReservation
    from .models.train_station import TrainStation
    from .models.train_trip import TrainTrip
    from .models.transfer_action import TransferAction
    from .models.travel_action import TravelAction
    from .models.travel_agency import TravelAgency
    from .models.treatment_indication import TreatmentIndication
    from .models.trip import Trip
    from .models.type_and_quantity_node import TypeAndQuantityNode
    from .models.un_register_action import UnRegisterAction
    from .models.unit_price_specification import UnitPriceSpecification
    from .models.update_action import UpdateAction
    from .models.use_action import UseAction
    from .models.user_blocks import UserBlocks
    from .models.user_checkins import UserCheckins
    from .models.user_comments import UserComments
    from .models.user_downloads import UserDownloads
    from .models.user_interaction import UserInteraction
    from .models.user_likes import UserLikes
    from .models.user_page_visits import UserPageVisits
    from .models.user_plays import UserPlays
    from .models.user_plus_ones import UserPlusOnes
    from .models.user_review import UserReview
    from .models.user_tweets import UserTweets
    from .models.vacation_rental import VacationRental
    from .models.vehicle import Vehicle
    from .models.vein import Vein
    from .models.vessel import Vessel
    from .models.veterinary_care import VeterinaryCare
    from .models.video_gallery import VideoGallery
    from .models.video_game import VideoGame
    from .models.video_game_clip import VideoGameClip
    from .models.video_game_series import VideoGameSeries
    from .models.video_object import VideoObject
    from .models.video_object_snapshot import VideoObjectSnapshot
    from .models.view_action import ViewAction
    from .models.virtual_location import VirtualLocation
    from .models.visual_arts_event import VisualArtsEvent
    from .models.visual_artwork import VisualArtwork
    from .models.vital_sign import VitalSign
    from .models.volcano import Volcano
    from .models.vote_action import VoteAction
    from .models.wp_ad_block import WPAdBlock
    from .models.wp_footer import WPFooter
    from .models.wp_header import WPHeader
    from .models.wp_side_bar import WPSideBar
    from .models.want_action import WantAction
    from .models.warranty_promise import WarrantyPromise
    from .models.watch_action import WatchAction
    from .models.waterfall import Waterfall
    from .models.wear_action import WearAction
    from .models.web_api import WebAPI
    from .models.web_application import WebApplication
    from .models.web_content import WebContent
    from .models.web_page import WebPage
    from .models.web_page_element import WebPageElement
    from .models.web_site import WebSite
    from .models.wholesale_store import WholesaleStore
    from .models.win_action import WinAction
    from .models.winery import Winery
    from .models.work_based_program import WorkBasedProgram
    from .models.workers_union import WorkersUnion
    from .models.write_action import WriteAction
    from .models.zoo import Zoo

_MODEL_MODULES = {
    'ThreeDModel': 'three_d_model',
    'AMRadioChannel': 'am_radio_channel',
    'APIReference': 'api_reference',
    'AboutPage': 'about_page',
    'AcceptAction': 'accept_action',
    'Accommodation': 'accommodation',
    'AccountingService': 'accounting_service',
    'AchieveAction': 'achieve_action',
    'Action': 'action',
    'ActionAccessSpecification': 'action_access_specification',
    'ActivateAction': 'activate_action',
    'AddAction': 'add_action',
    'AdministrativeArea': 'administrative_area',
    'AdultEntertainment': 'adult_entertainment',
    'AdvertiserContentArticle': 'advertiser_content_article',
    'AggregateOffer': 'aggregate_offer',
    'AggregateRating': 'aggregate_rating',
    'AgreeAction': 'agree_action',
    'Airline': 'airline',
    'Airport': 'airport',
    'AlignmentObject': 'alignment_object',
    'AllocateAction': 'allocate_action',
    'AmpStory': 'amp_story',
    'AmusementPark': 'amusement_park',
    'AnalysisNewsArticle': 'analysis_news_article',
    'AnatomicalStructure': 'anatomical_structure',
    'AnatomicalSystem': 'anatomical_system',
    'AnimalShelter': 'animal_shelter',
    'Answer': 'answer',
    'Apartment': 'apartment',
    'ApartmentComplex': 'apartment_complex',
    'AppendAction': 'append_action',
    'ApplyAction': 'apply_action',
    'ApprovedIndication': 'approved_indication',
    'Aquarium': 'aquarium',
    'ArchiveComponent': 'archive_component',
    'ArchiveOrganization': 'archive_organization',
    'ArriveAction': 'arrive_action',
    'ArtGallery': 'art_gallery',
    'Artery': 'artery',
    'Article': 'article',
    'AskAction': 'ask_action',
    'AskPublicNewsArticle': 'ask_public_news_article',
    'AssessAction': 'assess_action',
    'AssignAction': 'assign_action',
    'Atlas': 'atlas',
    'Attorney': 'attorney',
    'Audience': 'audience',
    'AudioObject': 'audio_object',
    'AudioObjectSnapshot': 'audio_object_snapshot',
    'Audiobook': 'audiobook',
    'AuthenticateAction': 'authenticate_action',
    'AuthorizeAction': 'authorize_action',
    'AutoBodyShop': 'auto_body_shop',
    'AutoDealer': 'auto_dealer',
    'AutoPartsStore': 'auto_parts_store',
    'AutoRental': 'auto_rental',
    'AutoRepair': 'auto_repair',
    'AutoWash': 'auto_wash',
    'AutomatedTeller': 'automated_teller',
    'AutomotiveBusiness': 'automotive_business',
    'BackgroundNewsArticle': 'background_news_article',
    'Bakery': 'bakery',
    'BankAccount': 'bank_account',
    'BankOrCreditUnion': 'bank_or_credit_union',
    'BarOrPub': 'bar_or_pub',
    'Barcode': 'barcode',
    'Beach': 'beach',
    'BeautySalon': 'beauty_salon',
    'BedAndBreakfast': 'bed_and_breakfast',
    'BedDetails': 'bed_details',
    'BefriendAction': 'befriend_action',
    'BikeStore': 'bike_store',
    'BioChemEntity': 'bio_chem_entity',
    'Blog': 'blog',
    'BlogPosting': 'blog_posting',
    'BloodTest': 'blood_test',
    'BoatReservation': 'boat_reservation',
    'BoatTerminal': 'boat_terminal',
    'BoatTrip': 'boat_trip',
    'BodyOfWater': 'body_of_water',
    'Bone': 'bone',
    'Book': 'book',
    'BookSeries': 'book_series',
    'BookStore': 'book_store',
    'BookmarkAction': 'bookmark_action',
    'BorrowAction': 'borrow_action',
    'BowlingAlley': 'bowling_alley',
    'BrainStructure': 'brain_structure',
    'Brand': 'brand',
    'BreadcrumbList': 'breadcrumb_list',
    'Brewery': 'brewery',
    'Bridge': 'bridge',
    'BroadcastChannel': 'broadcast_channel',
    'BroadcastEvent': 'broadcast_event',
    'BroadcastFrequencySpecification': 'broadcast_frequency_specification',
    'BroadcastService': 'broadcast_service',
    'BrokerageAccount': 'brokerage_account',
    'BuddhistTemple': 'buddhist_temple',
    'BusOrCoach': 'bus_or_coach',
    'BusReservation': 'bus_reservation',
    'BusStation': 'bus_station',
    'BusStop': 'bus_stop',
    'BusTrip': 'bus_trip',
    'BusinessAudience': 'business_audience',
    'BusinessEvent': 'business_event',
    'BuyAction': 'buy_action',
    'CDCPMDRecord': 'cdcpmd_record',
    'CableOrSatelliteService': 'cable_or_satellite_service',
    'CafeOrCoffeeShop': 'cafe_or_coffee_shop',
    'Campground': 'campground',
    'CampingPitch': 'camping_pitch',
    'Canal': 'canal',
    'CancelAction': 'cancel_action',
    'Car': 'car',
    'Casino': 'casino',
    'CategoryCode': 'category_code',
    'CategoryCodeSet': 'category_code_set',
    'CatholicChurch': 'catholic_church',
    'Cemetery': 'cemetery',
    'Certification': 'certification',
    'Chapter': 'chapter',
    'CheckAction': 'check_action',
    'CheckInAction': 'check_in_action',
    'CheckOutAction': 'check_out_action',
    'CheckoutPage': 'checkout_page',
    'ChemicalSubstance': 'chemical_substance',
    'ChildCare': 'child_care',
    'ChildrensEvent': 'childrens_event',
    'ChooseAction': 'choose_action',
    'Church': 'church',
    'City': 'city',
    'CityHall': 'city_hall',
    'CivicStructure': 'civic_structure',
    'Claim': 'claim',
    'ClaimReview': 'claim_review',
    'Class': 'class_',
    'Clip': 'clip',
    'ClothingStore': 'clothing_store',
    'Code': 'code',
    'Collection': 'collection',
    'CollectionPage': 'collection_page',
    'CollegeOrUniversity': 'college_or_university',
    'ComedyClub': 'comedy_club',
    'ComedyEvent': 'comedy_event',
    'ComicCoverArt': 'comic_cover_art',
    'ComicIssue': 'comic_issue',
    'ComicSeries': 'comic_series',
    'ComicStory': 'comic_story',
    'Comment': 'comment',
    'CommentAction': 'comment_action',
    'CommunicateAction': 'communicate_action',
    'CompleteDataFeed': 'complete_data_feed',
    'CompoundPriceSpecification': 'compound_price_specification',
    'ComputerLanguage': 'computer_language',
    'ComputerStore': 'computer_store',
    'ConferenceEvent': 'conference_event',
    'ConfirmAction': 'confirm_action',
    'Consortium': 'consortium',
    'ConstraintNode': 'constraint_node',
    'ConsumeAction': 'consume_action',
    'ContactPage': 'contact_page',
    'ContactPoint': 'contact_point',
    'Continent': 'continent',
    'ControlAction': 'control_action',
    'ConvenienceStore': 'convenience_store',
    'Conversation': 'conversation',
    'CookAction': 'cook_action',
    'Cooperative': 'cooperative',
    'Corporation': 'corporation',
    'CorrectionComment': 'correction_comment',
    'Country': 'country',
    'Course': 'course',
    'CourseInstance': 'course_instance',
    'Courthouse': 'courthouse',
    'CoverArt': 'cover_art',
    'CovidTestingFacility': 'covid_testing_facility',
    'CreateAction': 'create_action',
    'CreativeWork': 'creative_work',
    'CreativeWorkSeason': 'creative_work_season',
    'CreativeWorkSeries': 'creative_work_series',
    'Credential': 'credential',
    'CreditCard': 'credit_card',
    'Crematorium': 'crematorium',
    'CriticReview': 'critic_review',
    'CurrencyConversionService': 'currency_conversion_service',
    'DDxElement': 'd_dx_element',
    'DanceEvent': 'dance_event',
    'DanceGroup': 'dance_group',
    'DataCatalog': 'data_catalog',
    'DataDownload': 'data_download',
    'DataFeed': 'data_feed',
    'DataFeedItem': 'data_feed_item',
    'Dataset': 'dataset',
    'DatedMoneySpecification': 'dated_money_specification',
    'DaySpa': 'day_spa',
    'DeactivateAction': 'deactivate_action',
    'DefenceEstablishment': 'defence_establishment',
    'DefinedRegion': 'defined_region',
    'DefinedTerm': 'defined_term',
    'DefinedTermSet': 'defined_term_set',
    'DeleteAction': 'delete_action',
    'DeliveryChargeSpecification': 'delivery_charge_specification',
    'DeliveryEvent': 'delivery_event',
    'DeliveryTimeSettings': 'delivery_time_settings',
    'Demand': 'demand',
    'Dentist': 'dentist',
    'DepartAction': 'depart_action',
    'DepartmentStore': 'department_store',
    'DepositAccount': 'deposit_account',
    'DiagnosticLab': 'diagnostic_lab',
    'DiagnosticProcedure': 'diagnostic_procedure',
    'Diet': 'diet',
    'DietarySupplement': 'dietary_supplement',
    'DigitalDocument': 'digital_document',
    'DigitalDocumentPermission': 'digital_document_permission',
    'DisagreeAction': 'disagree_action',
    'DiscoverAction': 'discover_action',
    'DiscussionForumPosting': 'discussion_forum_posting',
    'DislikeAction': 'dislike_action',
    'Distillery': 'distillery',
    'DonateAction': 'donate_action',
    'DoseSchedule': 'dose_schedule',
    'DownloadAction': 'download_action',
    'DrawAction': 'draw_action',
    'Drawing': 'drawing',
    'DrinkAction': 'drink_action',
    'Drug': 'drug',
    'DrugClass': 'drug_class',
    'DrugCost': 'drug_cost',
    'DrugLegalStatus': 'drug_legal_status',
    'DrugStrength': 'drug_strength',
    'DryCleaningOrLaundry': 'dry_cleaning_or_laundry',
    'EatAction': 'eat_action',
    'EducationEvent': 'education_event',
    'EducationalAudience': 'educational_audience',
    'EducationalOccupationalCredential': 'educational_occupational_credential',
    'EducationalOccupationalProgram': 'educational_occupational_program',
    'EducationalOrganization': 'educational_organization',
    'Electrician': 'electrician',
    'ElectronicsStore': 'electronics_store',
    'ElementarySchool': 'elementary_school',
    'EmailMessage': 'email_message',
    'Embassy': 'embassy',
    'EmergencyService': 'emergency_service',
    'EmployeeRole': 'employee_role',
    'EmployerAggregateRating': 'employer_aggregate_rating',
    'EmployerReview': 'employer_review',
    'EmploymentAgency': 'employment_agency',
    'EndorseAction': 'endorse_action',
    'EndorsementRating': 'endorsement_rating',
    'EnergyConsumptionDetails': 'energy_consumption_details',
    'EngineSpecification': 'engine_specification',
    'EntertainmentBusiness': 'entertainment_business',
    'EntryPoint': 'entry_point',
    'Episode': 'episode',
    'Error': 'error',
    'Event': 'event',
    'EventReservation': 'event_reservation',
    'EventSeries': 'event_series',
    'EventVenue': 'event_venue',
    'ExchangeRateSpecification': 'exchange_rate_specification',
    'ExerciseAction': 'exercise_action',
    'ExerciseGym': 'exercise_gym',
    'ExercisePlan': 'exercise_plan',
    'ExhibitionEvent': 'exhibition_event',
    'FAQPage': 'faq_page',
    'FMRadioChannel': 'fm_radio_channel',
    'FastFoodRestaurant': 'fast_food_restaurant',
    'Festival': 'festival',
    'FilmAction': 'film_action',
    'FinancialIncentive': 'financial_incentive',
    'FinancialProduct': 'financial_product',
    'FinancialService': 'financial_service',
    'FindAction': 'find_action',
    'FireStation': 'fire_station',
    'Flight': 'flight',
    'FlightReservation': 'flight_reservation',
    'FloorPlan': 'floor_plan',
    'Florist': 'florist',
    'FollowAction': 'follow_action',
    'FoodEstablishment': 'food_establishment',
    'FoodEstablishmentReservation': 'food_establishment_reservation',
    'FoodEvent': 'food_event',
    'FoodService': 'food_service',
    'FundingAgency': 'funding_agency',
    'FundingScheme': 'funding_scheme',
    'FurnitureStore': 'furniture_store',
    'Game': 'game',
    'GameServer': 'game_server',
    'GardenStore': 'garden_store',
    'GasStation': 'gas_station',
    'GatedResidenceCommunity': 'gated_residence_community',
    'Gene': 'gene',
    'GeneralContractor': 'general_contractor',
    'GeoCircle': 'geo_circle',
    'GeoCoordinates': 'geo_coordinates',
    'GeoShape': 'geo_shape',
    'GeospatialGeometry': 'geospatial_geometry',
    'GiveAction': 'give_action',
    'GolfCourse': 'golf_course',
    'GovernmentBuilding': 'government_building',
    'GovernmentOffice': 'government_office',
    'GovernmentOrganization': 'government_organization',
    'GovernmentPermit': 'government_permit',
    'GovernmentService': 'government_service',
    'Grant': 'grant',
    'GroceryStore': 'grocery_store',
    'Guide': 'guide',
    'HVACBusiness': 'hvac_business',
    'Hackathon': 'hackathon',
    'HairSalon': 'hair_salon',
    'HardwareStore': 'hardware_store',
    'HealthAndBeautyBusiness': 'health_and_beauty_business',
    'HealthClub': 'health_club',
    'HealthInsurancePlan': 'health_insurance_plan',
    'HealthPlanCostSharingSpecification': 'health_plan_cost_sharing_specification',
    'HealthPlanFormulary': 'health_plan_formulary',
    'HealthPlanNetwork': 'health_plan_network',
    'HealthTopicContent': 'health_topic_content',
    'HighSchool': 'high_school',
    'HinduTemple': 'hindu_temple',
    'HobbyShop': 'hobby_shop',
    'HomeAndConstructionBusiness': 'home_and_construction_business',
    'HomeGoodsStore': 'home_goods_store',
    'Hospital': 'hospital',
    'Hostel': 'hostel',
    'Hotel': 'hotel',
    'HotelRoom': 'hotel_room',
    'House': 'house',
    'HousePainter': 'house_painter',
    'HowTo': 'how_to',
    'HowToDirection': 'how_to_direction',
    'HowToItem': 'how_to_item',
    'HowToSection': 'how_to_section',
    'HowToStep': 'how_to_step',
    'HowToSupply': 'how_to_supply',
    'HowToTip': 'how_to_tip',
    'HowToTool': 'how_to_tool',
    'HyperToc': 'hyper_toc',
    'HyperTocEntry': 'hyper_toc_entry',
    'IceCreamShop': 'ice_cream_shop',
    'IgnoreAction': 'ignore_action',
    'ImageGallery': 'image_gallery',
    'ImageObject': 'image_object',
    'ImageObjectSnapshot': 'image_object_snapshot',
    'ImagingTest': 'imaging_test',
    'IndividualPhysician': 'individual_physician',
    'IndividualProduct': 'individual_product',
    'InfectiousDisease': 'infectious_disease',
    'InformAction': 'inform_action',
    'InsertAction': 'insert_action',
    'InstallAction': 'install_action',
    'InstantaneousEvent': 'instantaneous_event',
    'InsuranceAgency': 'insurance_agency',
    'Intangible': 'intangible',
    'InteractAction': 'interact_action',
    'InteractionCounter': 'interaction_counter',
    'InternetCafe': 'internet_cafe',
    'InvestmentFund': 'investment_fund',
    'InvestmentOrDeposit': 'investment_or_deposit',
    'InviteAction': 'invite_action',
    'Invoice': 'invoice',
    'ItemList': 'item_list',
    'ItemPage': 'item_page',
    'JewelryStore': 'jewelry_store',
    'JobPosting': 'job_posting',
    'JoinAction': 'join_action',
    'Joint': 'joint',
    'LakeBodyOfWater': 'lake_body_of_water',
    'Landform': 'landform',
    'LandmarksOrHistoricalBuildings': 'landmarks_or_historical_buildings',
    'Language': 'language',
    'LearningResource': 'learning_resource',
    'LeaveAction': 'leave_action',
    'LegalService': 'legal_service',
    'Legislation': 'legislation',
    'LegislationObject': 'legislation_object',
    'LegislativeBuilding': 'legislative_building',
    'LendAction': 'lend_action',
    'Library': 'library',
    'LibrarySystem': 'library_system',
    'LifestyleModification': 'lifestyle_modification',
    'Ligament': 'ligament',
    'LikeAction': 'like_action',
    'LinkRole': 'link_role',
    'LiquorStore': 'liquor_store',
    'ListItem': 'list_item',
    'ListenAction': 'listen_action',
    'LiteraryEvent': 'literary_event',
    'LiveBlogPosting': 'live_blog_posting',
    'LoanOrCredit': 'loan_or_credit',
    'LocalBusiness': 'local_business',
    'LocationFeatureSpecification': 'location_feature_specification',
    'Locksmith': 'locksmith',
    'LodgingBusiness': 'lodging_business',
    'LodgingReservation': 'lodging_reservation',
    'LoginAction': 'login_action',
    'LoseAction': 'lose_action',
    'LymphaticVessel': 'lymphatic_vessel',
    'Manuscript': 'manuscript',
    'Map': 'map',
    'MarryAction': 'marry_action',
    'MathSolver': 'math_solver',
    'MaximumDoseSchedule': 'maximum_dose_schedule',
    'MediaGallery': 'media_gallery',
    'MediaObject': 'media_object',
    'MediaReview': 'media_review',
    'MediaReviewItem': 'media_review_item',
    'MediaSubscription': 'media_subscription',
    'MedicalAudience': 'medical_audience',
    'MedicalBusiness': 'medical_business',
    'MedicalCause': 'medical_cause',
    'MedicalClinic': 'medical_clinic',
    'MedicalCode': 'medical_code',
    'MedicalCondition': 'medical_condition',
    'MedicalConditionStage': 'medical_condition_stage',
    'MedicalContraindication': 'medical_contraindication',
    'MedicalDevice': 'medical_device',
    'MedicalEntity': 'medical_entity',
    'MedicalGuideline': 'medical_guideline',
    'MedicalGuidelineContraindication': 'medical_guideline_contraindication',
    'MedicalGuidelineRecommendation': 'medical_guideline_recommendation',
    'MedicalIndication': 'medical_indication',
    'MedicalIntangible': 'medical_intangible',
    'MedicalObservationalStudy': 'medical_observational_study',
    'MedicalOrganization': 'medical_organization',
    'MedicalProcedure': 'medical_procedure',
    'MedicalRiskCalculator': 'medical_risk_calculator',
    'MedicalRiskEstimator': 'medical_risk_estimator',
    'MedicalRiskFactor': 'medical_risk_factor',
    'MedicalRiskScore': 'medical_risk_score',
    'MedicalScholarlyArticle': 'medical_scholarly_article',
    'MedicalSign': 'medical_sign',
    'MedicalSignOrSymptom': 'medical_sign_or_symptom',
    'MedicalStudy': 'medical_study',
    'MedicalSymptom': 'medical_symptom',
    'MedicalTest': 'medical_test',
    'MedicalTestPanel': 'medical_test_panel',
    'MedicalTherapy': 'medical_therapy',
    'MedicalTrial': 'medical_trial',
    'MedicalWebPage': 'medical_web_page',
    'MeetingRoom': 'meeting_room',
    'MemberProgram': 'member_program',
    'MemberProgramTier': 'member_program_tier',
    'MensClothingStore': 'mens_clothing_store',
    'Menu': 'menu',
    'MenuItem': 'menu_item',
    'MenuSection': 'menu_section',
    'MerchantReturnPolicy': 'merchant_return_policy',
    'MerchantReturnPolicySeasonalOverride': 'merchant_return_policy_seasonal_override',
    'Message': 'message',
    'MiddleSchool': 'middle_school',
    'MobileApplication': 'mobile_application',
    'MobilePhoneStore': 'mobile_phone_store',
    'MolecularEntity': 'molecular_entity',
    'MonetaryAmount': 'monetary_amount',
    'MonetaryAmountDistribution': 'monetary_amount_distribution',
    'MonetaryGrant': 'monetary_grant',
    'MoneyTransfer': 'money_transfer',
    'MortgageLoan': 'mortgage_loan',
    'Mosque': 'mosque',
    'Motel': 'motel',
    'Motorcycle': 'motorcycle',
    'MotorcycleDealer': 'motorcycle_dealer',
    'MotorcycleRepair': 'motorcycle_repair',
    'MotorizedBicycle': 'motorized_bicycle',
    'Mountain': 'mountain',
    'MoveAction': 'move_action',
    'Movie': 'movie',
    'MovieClip': 'movie_clip',
    'MovieRentalStore': 'movie_rental_store',
    'MovieSeries': 'movie_series',
    'MovieTheater': 'movie_theater',
    'MovingCompany': 'moving_company',
    'Muscle': 'muscle',
    'Museum': 'museum',
    'MusicAlbum': 'music_album',
    'MusicComposition': 'music_composition',
    'MusicEvent': 'music_event',
    'MusicGroup': 'music_group',
    'MusicPlaylist': 'music_playlist',
    'MusicRecording': 'music_recording',
    'MusicRelease': 'music_release',
    'MusicStore': 'music_store',
    'MusicVenue': 'music_venue',
    'MusicVideoObject': 'music_video_object',
    'NGO': 'ngo',
    'NailSalon': 'nail_salon',
    'Nerve': 'nerve',
    'NewsArticle': 'news_article',
    'NewsMediaOrganization': 'news_media_organization',
    'Newspaper': 'newspaper',
    'NightClub': 'night_club',
    'Notary': 'notary',
    'NoteDigitalDocument': 'note_digital_document',
    'NutritionInformation': 'nutrition_information',
    'Observation': 'observation',
    'Occupation': 'occupation',
    'OccupationalExperienceRequirements': 'occupational_experience_requirements',
    'OccupationalTherapy': 'occupational_therapy',
    'OceanBodyOfWater': 'ocean_body_of_water',
    'Offer': 'offer',
    'OfferCatalog': 'offer_catalog',
    'OfferForLease': 'offer_for_lease',
    'OfferForPurchase': 'offer_for_purchase',
    'OfferShippingDetails': 'offer_shipping_details',
    'OfficeEquipmentStore': 'office_equipment_store',
    'OnDemandEvent': 'on_demand_event',
    'OnlineBusiness': 'online_business',
    'OnlineMarketplace': 'online_marketplace',
    'OnlineStore': 'online_store',
    'OpeningHoursSpecification': 'opening_hours_specification',
    'OperatingSystem': 'operating_system',
    'OpinionNewsArticle': 'opinion_news_article',
    'Optician': 'optician',
    'Order': 'order',
    'OrderAction': 'order_action',
    'OrderItem': 'order_item',
    'Organization': 'organization',
    'OrganizationRole': 'organization_role',
    'OrganizeAction': 'organize_action',
    'OutletStore': 'outlet_store',
    'OwnershipInfo': 'ownership_info',
    'PaintAction': 'paint_action',
    'Painting': 'painting',
    'PalliativeProcedure': 'palliative_procedure',
    'ParcelDelivery': 'parcel_delivery',
    'ParentAudience': 'parent_audience',
    'Park': 'park',
    'ParkingFacility': 'parking_facility',
    'PathologyTest': 'pathology_test',
    'Patient': 'patient',
    'PawnShop': 'pawn_shop',
    'PayAction': 'pay_action',
    'PaymentCard': 'payment_card',
    'PaymentChargeSpecification': 'payment_charge_specification',
    'PaymentMethod': 'payment_method',
    'PaymentService': 'payment_service',
    'PeopleAudience': 'people_audience',
    'PerformAction': 'perform_action',
    'PerformanceRole': 'performance_role',
    'PerformingArtsEvent': 'performing_arts_event',
    'PerformingArtsTheater': 'performing_arts_theater',
    'PerformingGroup': 'performing_group',
    'Periodical': 'periodical',
    'Permit': 'permit',
    'Person': 'person',
    'PetStore': 'pet_store',
    'Pharmacy': 'pharmacy',
    'Photograph': 'photograph',
    'PhotographAction': 'photograph_action',
    'PhysicalActivity': 'physical_activity',
    'PhysicalTherapy': 'physical_therapy',
    'Physician': 'physician',
    'PhysiciansOffice': 'physicians_office',
    'Place': 'place',
    'PlaceOfWorship': 'place_of_worship',
    'PlanAction': 'plan_action',
    'Play': 'play',
    'PlayAction': 'play_action',
    'PlayGameAction': 'play_game_action',
    'Playground': 'playground',
    'Plumber': 'plumber',
    'PodcastEpisode': 'podcast_episode',
    'PodcastSeason': 'podcast_season',
    'PodcastSeries': 'podcast_series',
    'PoliceStation': 'police_station',
    'PoliticalParty': 'political_party',
    'Pond': 'pond',
    'PostOffice': 'post_office',
    'PostalAddress': 'postal_address',
    'PostalCodeRangeSpecification': 'postal_code_range_specification',
    'Poster': 'poster',
    'PreOrderAction': 'pre_order_action',
    'PrependAction': 'prepend_action',
    'Preschool': 'preschool',
    'PresentationDigitalDocument': 'presentation_digital_document',
    'PreventionIndication': 'prevention_indication',
    'PriceSpecification': 'price_specification',
    'Product': 'product',
    'ProductCollection': 'product_collection',
    'ProductGroup': 'product_group',
    'ProductModel': 'product_model',
    'ProductReturnPolicy': 'product_return_policy',
    'ProfessionalService': 'professional_service',
    'ProfilePage': 'profile_page',
    'ProgramMembership': 'program_membership',
    'Project': 'project',
    'Property': 'property',
    'PropertyValue': 'property_value',
    'PropertyValueSpecification': 'property_value_specification',
    'Protein': 'protein',
    'PsychologicalTreatment': 'psychological_treatment',
    'PublicSwimmingPool': 'public_swimming_pool',
    'PublicToilet': 'public_toilet',
    'PublicationEvent': 'publication_event',
    'PublicationIssue': 'publication_issue',
    'PublicationVolume': 'publication_volume',
    'QAPage': 'qa_page',
    'QuantitativeValue': 'quantitative_value',
    'QuantitativeValueDistribution': 'quantitative_value_distribution',
    'Question': 'question',
    'Quiz': 'quiz',
    'Quotation': 'quotation',
    'QuoteAction': 'quote_action',
    'RVPark': 'rv_park',
    'RadiationTherapy': 'radiation_therapy',
    'RadioBroadcastService': 'radio_broadcast_service',
    'RadioChannel': 'radio_channel',
    'RadioClip': 'radio_clip',
    'RadioEpisode': 'radio_episode',
    'RadioSeason': 'radio_season',
    'RadioSeries': 'radio_series',
    'RadioStation': 'radio_station',
    'Rating': 'rating',
    'ReactAction': 'react_action',
    'ReadAction': 'read_action',
    'RealEstateAgent': 'real_estate_agent',
    'RealEstateListing': 'real_estate_listing',
    'ReceiveAction': 'receive_action',
    'Recipe': 'recipe',
    'Recommendation': 'recommendation',
    'RecommendedDoseSchedule': 'recommended_dose_schedule',
    'RecyclingCenter': 'recycling_center',
    'RegisterAction': 'register_action',
    'RejectAction': 'reject_action',
    'RentAction': 'rent_action',
    'RentalCarReservation': 'rental_car_reservation',
    'RepaymentSpecification': 'repayment_specification',
    'ReplaceAction': 'replace_action',
    'ReplyAction': 'reply_action',
    'Report': 'report',
    'ReportageNewsArticle': 'reportage_news_article',
    'ReportedDoseSchedule': 'reported_dose_schedule',
    'ResearchOrganization': 'research_organization',
    'ResearchProject': 'research_project',
    'Researcher': 'researcher',
    'Reservation': 'reservation',
    'ReservationPackage': 'reservation_package',
    'ReserveAction': 'reserve_action',
    'Reservoir': 'reservoir',
    'ResetPasswordAction': 'reset_password_action',
    'Residence': 'residence',
    'Resort': 'resort',
    'Restaurant': 'restaurant',
    'ResumeAction': 'resume_action',
    'ReturnAction': 'return_action',
    'Review': 'review',
    'ReviewAction': 'review_action',
    'ReviewNewsArticle': 'review_news_article',
    'RiverBodyOfWater': 'river_body_of_water',
    'Role': 'role',
    'RoofingContractor': 'roofing_contractor',
    'Room': 'room',
    'RsvpAction': 'rsvp_action',
    'RuntimePlatform': 'runtime_platform',
    'SaleEvent': 'sale_event',
    'SatiricalArticle': 'satirical_article',
    'Schedule': 'schedule',
    'ScheduleAction': 'schedule_action',
    'ScholarlyArticle': 'scholarly_article',
    'School': 'school',
    'SchoolDistrict': 'school_district',
    'ScreeningEvent': 'screening_event',
    'Sculpture': 'sculpture',
    'SeaBodyOfWater': 'sea_body_of_water',
    'SearchAction': 'search_action',
    'SearchRescueOrganization': 'search_rescue_organization',
    'SearchResultsPage': 'search_results_page',
    'Season': 'season',
    'Seat': 'seat',
    'SeekToAction': 'seek_to_action',
    'SelfStorage': 'self_storage',
    'SellAction': 'sell_action',
    'SendAction': 'send_action',
    'SequentialArt': 'sequential_art',
    'Series': 'series',
    'Service': 'service',
    'ServiceChannel': 'service_channel',
    'ServicePeriod': 'service_period',
    'ShareAction': 'share_action',
    'SheetMusic': 'sheet_music',
    'ShippingConditions': 'shipping_conditions',
    'ShippingDeliveryTime': 'shipping_delivery_time',
    'ShippingRateSettings': 'shipping_rate_settings',
    'ShippingService': 'shipping_service',
    'ShoeStore': 'shoe_store',
    'ShoppingCenter': 'shopping_center',
    'ShortStory': 'short_story',
    'SingleFamilyResidence': 'single_family_residence',
    'SiteNavigationElement': 'site_navigation_element',
    'SkiResort': 'ski_resort',
    'SocialEvent': 'social_event',
    'SocialMediaPosting': 'social_media_posting',
    'SoftwareApplication': 'software_application',
    'SoftwareSourceCode': 'software_source_code',
    'SolveMathAction': 'solve_math_action',
    'SomeProducts': 'some_products',
    'SpeakableSpecification': 'speakable_specification',
    'SpecialAnnouncement': 'special_announcement',
    'SportingGoodsStore': 'sporting_goods_store',
    'SportsActivityLocation': 'sports_activity_location',
    'SportsClub': 'sports_club',
    'SportsEvent': 'sports_event',
    'SportsOrganization': 'sports_organization',
    'SportsTeam': 'sports_team',
    'SpreadsheetDigitalDocument': 'spreadsheet_digital_document',
    'StadiumOrArena': 'stadium_or_arena',
    'State': 'state',
    'Statement': 'statement',
    'StatisticalPopulation': 'statistical_population',
    'StatisticalVariable': 'statistical_variable',
    'Store': 'store',
    'StructuredValue': 'structured_value',
    'StupidType': 'stupid_type',
    'SubscribeAction': 'subscribe_action',
    'Substance': 'substance',
    'SubwayStation': 'subway_station',
    'Suite': 'suite',
    'SuperficialAnatomy': 'superficial_anatomy',
    'SurgicalProcedure': 'surgical_procedure',
    'SuspendAction': 'suspend_action',
    'Syllabus': 'syllabus',
    'Synagogue': 'synagogue',
    'TVClip': 'tv_clip',
    'TVEpisode': 'tv_episode',
    'TVSeason': 'tv_season',
    'TVSeries': 'tv_series',
    'Table': 'table',
    'TakeAction': 'take_action',
    'TattooParlor': 'tattoo_parlor',
    'Taxi': 'taxi',
    'TaxiReservation': 'taxi_reservation',
    'TaxiService': 'taxi_service',
    'TaxiStand': 'taxi_stand',
    'Taxon': 'taxon',
    'TechArticle': 'tech_article',
    'TelevisionChannel': 'television_channel',
    'TelevisionStation': 'television_station',
    'TennisComplex': 'tennis_complex',
    'TextDigitalDocument': 'text_digital_document',
    'TextObject': 'text_object',
    'TheaterEvent': 'theater_event',
    'TheaterGroup': 'theater_group',
    'TherapeuticProcedure': 'therapeutic_procedure',
    'Thesis': 'thesis',
    'Thing': 'thing',
    'Ticket': 'ticket',
    'TieAction': 'tie_action',
    'TipAction': 'tip_action',
    'TireShop': 'tire_shop',
    'TouristAttraction': 'tourist_attraction',
    'TouristDestination': 'tourist_destination',
    'TouristInformationCenter': 'tourist_information_center',
    'TouristTrip': 'tourist_trip',
    'ToyStore': 'toy_store',
    'TrackAction': 'track_action',
    'TradeAction': 'trade_action',
    'TrainReservation': 'train_reservation',
    'TrainStation': 'train_station',
    'TrainTrip': 'train_trip',
    'TransferAction': 'transfer_action',
    'TravelAction': 'travel_action',
    'TravelAgency': 'travel_agency',
    'TreatmentIndication': 'treatment_indication',
    'Trip': 'trip',
    'TypeAndQuantityNode': 'type_and_quantity_node',
    'UnRegisterAction': 'un_register_action',
    'UnitPriceSpecification': 'unit_price_specification',
    'UpdateAction': 'update_action',
    'UseAction': 'use_action',
    'UserBlocks': 'user_blocks',
    'UserCheckins': 'user_checkins',
    'UserComments': 'user_comments',
    'UserDownloads': 'user_downloads',
    'UserInteraction': 'user_interaction',
    'UserLikes': 'user_likes',
    'UserPageVisits': 'user_page_visits',
    'UserPlays': 'user_plays',
    'UserPlusOnes': 'user_plus_ones',
    'UserReview': 'user_review',
    'UserTweets': 'user_tweets',
    'VacationRental': 'vacation_rental',
    'Vehicle': 'vehicle',
    'Vein': 'vein',
    'Vessel': 'vessel',
    'VeterinaryCare': 'veterinary_care',
    'VideoGallery': 'video_gallery',
    'VideoGame': 'video_game',
    'VideoGameClip': 'video_game_clip',
    'VideoGameSeries': 'video_game_series',
    'VideoObject': 'video_object',
    'VideoObjectSnapshot': 'video_object_snapshot',
    'ViewAction': 'view_action',
    'VirtualLocation': 'virtual_location',
    'VisualArtsEvent': 'visual_arts_event',
    'VisualArtwork': 'visual_artwork',
    'VitalSign': 'vital_sign',
    'Volcano': 'volcano',
    'VoteAction': 'vote_action',
    'WPAdBlock': 'wp_ad_block',
    'WPFooter': 'wp_footer',
    'WPHeader': 'wp_header',
    'WPSideBar': 'wp_side_bar',
    'WantAction': 'want_action',
    'WarrantyPromise': 'warranty_promise',
    'WatchAction': 'watch_action',
    'Waterfall': 'waterfall',
    'WearAction': 'wear_action',
    'WebAPI': 'web_api',
    'WebApplication': 'web_application',
    'WebContent': 'web_content',
    'WebPage': 'web_page',
    'WebPageElement': 'web_page_element',
    'WebSite': 'web_site',
    'WholesaleStore': 'wholesale_store',
    'WinAction': 'win_action',
    'Winery': 'winery',
    'WorkBasedProgram': 'work_based_program',
    'WorkersUnion': 'workers_union',
    'WriteAction': 'write_action',
    'Zoo': 'zoo',
}
_ENUM_NAMES = {
    'ActionStatusType': 'ActionStatusType',
    'AdultOrientedEnumeration': 'AdultOrientedEnumeration',
    'BedType': 'BedType',
    'BoardingPolicyType': 'BoardingPolicyType',
    'BodyMeasurementTypeEnumeration': 'BodyMeasurementTypeEnumeration',
    'BookFormatType': 'BookFormatType',
    'BusinessEntityType': 'BusinessEntityType',
    'BusinessFunction': 'BusinessFunction',
    'CarUsageType': 'CarUsageType',
    'CertificationStatusEnumeration': 'CertificationStatusEnumeration',
    'ContactPointOption': 'ContactPointOption',
    'DENonprofitType': 'DENonprofitType',
    'DayOfWeek': 'DayOfWeek',
    'DeliveryMethod': 'DeliveryMethod',
    'DigitalDocumentPermissionType': 'DigitalDocumentPermissionType',
    'DigitalPlatformEnumeration': 'DigitalPlatformEnumeration',
    'DriveWheelConfigurationValue': 'DriveWheelConfigurationValue',
    'DrugCostCategory': 'DrugCostCategory',
    'DrugPregnancyCategory': 'DrugPregnancyCategory',
    'DrugPrescriptionStatus': 'DrugPrescriptionStatus',
    'EUEnergyEfficiencyEnumeration': 'EUEnergyEfficiencyEnumeration',
    'EnergyEfficiencyEnumeration': 'EnergyEfficiencyEnumeration',
    'EnergyStarEnergyEfficiencyEnumeration': 'EnergyStarEnergyEfficiencyEnumeration',
    'Enumeration': 'Enumeration',
    'EventAttendanceModeEnumeration': 'EventAttendanceModeEnumeration',
    'EventStatusType': 'EventStatusType',
    'FulfillmentTypeEnumeration': 'FulfillmentTypeEnumeration',
    'GameAvailabilityEnumeration': 'GameAvailabilityEnumeration',
    'GamePlayMode': 'GamePlayMode',
    'GameServerStatus': 'GameServerStatus',
    'GenderType': 'GenderType',
    'GovernmentBenefitsType': 'GovernmentBenefitsType',
    'HealthAspectEnumeration': 'HealthAspectEnumeration',
    'IPTCDigitalSourceEnumeration': 'IPTCDigitalSourceEnumeration',
    'ITNonprofitType': 'ITNonprofitType',
    'IncentiveQualifiedExpenseType': 'IncentiveQualifiedExpenseType',
    'IncentiveStatus': 'IncentiveStatus',
    'IncentiveType': 'IncentiveType',
    'InfectiousAgentClass': 'InfectiousAgentClass',
    'ItemAvailability': 'ItemAvailability',
    'ItemListOrderType': 'ItemListOrderType',
    'LegalForceStatus': 'LegalForceStatus',
    'LegalValueLevel': 'LegalValueLevel',
    'MapCategoryType': 'MapCategoryType',
    'MeasurementMethodEnum': 'MeasurementMethodEnum',
    'MeasurementTypeEnumeration': 'MeasurementTypeEnumeration',
    'MediaEnumeration': 'MediaEnumeration',
    'MediaManipulationRatingEnumeration': 'MediaManipulationRatingEnumeration',
    'MedicalAudienceType': 'MedicalAudienceType',
    'MedicalDevicePurpose': 'MedicalDevicePurpose',
    'MedicalEnumeration': 'MedicalEnumeration',
    'MedicalEvidenceLevel': 'MedicalEvidenceLevel',
    'MedicalImagingTechnique': 'MedicalImagingTechnique',
    'MedicalObservationalStudyDesign': 'MedicalObservationalStudyDesign',
    'MedicalProcedureType': 'MedicalProcedureType',
    'MedicalSpecialty': 'MedicalSpecialty',
    'MedicalStudyStatus': 'MedicalStudyStatus',
    'MedicalTrialDesign': 'MedicalTrialDesign',
    'MedicineSystem': 'MedicineSystem',
    'MerchantReturnEnumeration': 'MerchantReturnEnumeration',
    'MusicAlbumProductionType': 'MusicAlbumProductionType',
    'MusicAlbumReleaseType': 'MusicAlbumReleaseType',
    'MusicReleaseFormatType': 'MusicReleaseFormatType',
    'NLNonprofitType': 'NLNonprofitType',
    'NonprofitType': 'NonprofitType',
    'OfferItemCondition': 'OfferItemCondition',
    'OrderStatus': 'OrderStatus',
    'PaymentMethodType': 'PaymentMethodType',
    'PaymentStatusType': 'PaymentStatusType',
    'PhysicalActivityCategory': 'PhysicalActivityCategory',
    'PhysicalExam': 'PhysicalExam',
    'PriceComponentTypeEnumeration': 'PriceComponentTypeEnumeration',
    'PriceTypeEnumeration': 'PriceTypeEnumeration',
    'ProductReturnEnumeration': 'ProductReturnEnumeration',
    'PurchaseType': 'PurchaseType',
    'QualitativeValue': 'QualitativeValue',
    'RefundTypeEnumeration': 'RefundTypeEnumeration',
    'ReservationStatusType': 'ReservationStatusType',
    'RestrictedDiet': 'RestrictedDiet',
    'ReturnFeesEnumeration': 'ReturnFeesEnumeration',
    'ReturnLabelSourceEnumeration': 'ReturnLabelSourceEnumeration',
    'ReturnMethodEnumeration': 'ReturnMethodEnumeration',
    'RsvpResponseType': 'RsvpResponseType',
    'SizeGroupEnumeration': 'SizeGroupEnumeration',
    'SizeSpecification': 'SizeSpecification',
    'SizeSystemEnumeration': 'SizeSystemEnumeration',
    'Specialty': 'Specialty',
    'StatusEnumeration': 'StatusEnumeration',
    'SteeringPositionValue': 'SteeringPositionValue',
    'TierBenefitEnumeration': 'TierBenefitEnumeration',
    'UKNonprofitType': 'UKNonprofitType',
    'USNonprofitType': 'USNonprofitType',
    'WarrantyScope': 'WarrantyScope',
    'WearableMeasurementTypeEnumeration': 'WearableMeasurementTypeEnumeration',
    'WearableSizeGroupEnumeration': 'WearableSizeGroupEnumeration',
    'WearableSizeSystemEnumeration': 'WearableSizeSystemEnumeration',
}

def __getattr__(name: str):
    module_name = _MODEL_MODULES.get(name)
    if module_name is not None:
        model = getattr(import_module(f'.models.{module_name}', __name__), name)
        from . import registry
        return registry.rebuild(next(term for term, cls_name in registry._MODEL_CLASSES.items() if cls_name == name))
    enum_name = _ENUM_NAMES.get(name)
    if enum_name is not None:
        return getattr(import_module('.enums', __name__), enum_name)
    raise AttributeError(name)

__all__ = [
    'ThreeDModel',
    'AMRadioChannel',
    'APIReference',
    'AboutPage',
    'AcceptAction',
    'Accommodation',
    'AccountingService',
    'AchieveAction',
    'Action',
    'ActionAccessSpecification',
    'ActivateAction',
    'AddAction',
    'AdministrativeArea',
    'AdultEntertainment',
    'AdvertiserContentArticle',
    'AggregateOffer',
    'AggregateRating',
    'AgreeAction',
    'Airline',
    'Airport',
    'AlignmentObject',
    'AllocateAction',
    'AmpStory',
    'AmusementPark',
    'AnalysisNewsArticle',
    'AnatomicalStructure',
    'AnatomicalSystem',
    'AnimalShelter',
    'Answer',
    'Apartment',
    'ApartmentComplex',
    'AppendAction',
    'ApplyAction',
    'ApprovedIndication',
    'Aquarium',
    'ArchiveComponent',
    'ArchiveOrganization',
    'ArriveAction',
    'ArtGallery',
    'Artery',
    'Article',
    'AskAction',
    'AskPublicNewsArticle',
    'AssessAction',
    'AssignAction',
    'Atlas',
    'Attorney',
    'Audience',
    'AudioObject',
    'AudioObjectSnapshot',
    'Audiobook',
    'AuthenticateAction',
    'AuthorizeAction',
    'AutoBodyShop',
    'AutoDealer',
    'AutoPartsStore',
    'AutoRental',
    'AutoRepair',
    'AutoWash',
    'AutomatedTeller',
    'AutomotiveBusiness',
    'BackgroundNewsArticle',
    'Bakery',
    'BankAccount',
    'BankOrCreditUnion',
    'BarOrPub',
    'Barcode',
    'Beach',
    'BeautySalon',
    'BedAndBreakfast',
    'BedDetails',
    'BefriendAction',
    'BikeStore',
    'BioChemEntity',
    'Blog',
    'BlogPosting',
    'BloodTest',
    'BoatReservation',
    'BoatTerminal',
    'BoatTrip',
    'BodyOfWater',
    'Bone',
    'Book',
    'BookSeries',
    'BookStore',
    'BookmarkAction',
    'BorrowAction',
    'BowlingAlley',
    'BrainStructure',
    'Brand',
    'BreadcrumbList',
    'Brewery',
    'Bridge',
    'BroadcastChannel',
    'BroadcastEvent',
    'BroadcastFrequencySpecification',
    'BroadcastService',
    'BrokerageAccount',
    'BuddhistTemple',
    'BusOrCoach',
    'BusReservation',
    'BusStation',
    'BusStop',
    'BusTrip',
    'BusinessAudience',
    'BusinessEvent',
    'BuyAction',
    'CDCPMDRecord',
    'CableOrSatelliteService',
    'CafeOrCoffeeShop',
    'Campground',
    'CampingPitch',
    'Canal',
    'CancelAction',
    'Car',
    'Casino',
    'CategoryCode',
    'CategoryCodeSet',
    'CatholicChurch',
    'Cemetery',
    'Certification',
    'Chapter',
    'CheckAction',
    'CheckInAction',
    'CheckOutAction',
    'CheckoutPage',
    'ChemicalSubstance',
    'ChildCare',
    'ChildrensEvent',
    'ChooseAction',
    'Church',
    'City',
    'CityHall',
    'CivicStructure',
    'Claim',
    'ClaimReview',
    'Class',
    'Clip',
    'ClothingStore',
    'Code',
    'Collection',
    'CollectionPage',
    'CollegeOrUniversity',
    'ComedyClub',
    'ComedyEvent',
    'ComicCoverArt',
    'ComicIssue',
    'ComicSeries',
    'ComicStory',
    'Comment',
    'CommentAction',
    'CommunicateAction',
    'CompleteDataFeed',
    'CompoundPriceSpecification',
    'ComputerLanguage',
    'ComputerStore',
    'ConferenceEvent',
    'ConfirmAction',
    'Consortium',
    'ConstraintNode',
    'ConsumeAction',
    'ContactPage',
    'ContactPoint',
    'Continent',
    'ControlAction',
    'ConvenienceStore',
    'Conversation',
    'CookAction',
    'Cooperative',
    'Corporation',
    'CorrectionComment',
    'Country',
    'Course',
    'CourseInstance',
    'Courthouse',
    'CoverArt',
    'CovidTestingFacility',
    'CreateAction',
    'CreativeWork',
    'CreativeWorkSeason',
    'CreativeWorkSeries',
    'Credential',
    'CreditCard',
    'Crematorium',
    'CriticReview',
    'CurrencyConversionService',
    'DDxElement',
    'DanceEvent',
    'DanceGroup',
    'DataCatalog',
    'DataDownload',
    'DataFeed',
    'DataFeedItem',
    'Dataset',
    'DatedMoneySpecification',
    'DaySpa',
    'DeactivateAction',
    'DefenceEstablishment',
    'DefinedRegion',
    'DefinedTerm',
    'DefinedTermSet',
    'DeleteAction',
    'DeliveryChargeSpecification',
    'DeliveryEvent',
    'DeliveryTimeSettings',
    'Demand',
    'Dentist',
    'DepartAction',
    'DepartmentStore',
    'DepositAccount',
    'DiagnosticLab',
    'DiagnosticProcedure',
    'Diet',
    'DietarySupplement',
    'DigitalDocument',
    'DigitalDocumentPermission',
    'DisagreeAction',
    'DiscoverAction',
    'DiscussionForumPosting',
    'DislikeAction',
    'Distillery',
    'DonateAction',
    'DoseSchedule',
    'DownloadAction',
    'DrawAction',
    'Drawing',
    'DrinkAction',
    'Drug',
    'DrugClass',
    'DrugCost',
    'DrugLegalStatus',
    'DrugStrength',
    'DryCleaningOrLaundry',
    'EatAction',
    'EducationEvent',
    'EducationalAudience',
    'EducationalOccupationalCredential',
    'EducationalOccupationalProgram',
    'EducationalOrganization',
    'Electrician',
    'ElectronicsStore',
    'ElementarySchool',
    'EmailMessage',
    'Embassy',
    'EmergencyService',
    'EmployeeRole',
    'EmployerAggregateRating',
    'EmployerReview',
    'EmploymentAgency',
    'EndorseAction',
    'EndorsementRating',
    'EnergyConsumptionDetails',
    'EngineSpecification',
    'EntertainmentBusiness',
    'EntryPoint',
    'Episode',
    'Error',
    'Event',
    'EventReservation',
    'EventSeries',
    'EventVenue',
    'ExchangeRateSpecification',
    'ExerciseAction',
    'ExerciseGym',
    'ExercisePlan',
    'ExhibitionEvent',
    'FAQPage',
    'FMRadioChannel',
    'FastFoodRestaurant',
    'Festival',
    'FilmAction',
    'FinancialIncentive',
    'FinancialProduct',
    'FinancialService',
    'FindAction',
    'FireStation',
    'Flight',
    'FlightReservation',
    'FloorPlan',
    'Florist',
    'FollowAction',
    'FoodEstablishment',
    'FoodEstablishmentReservation',
    'FoodEvent',
    'FoodService',
    'FundingAgency',
    'FundingScheme',
    'FurnitureStore',
    'Game',
    'GameServer',
    'GardenStore',
    'GasStation',
    'GatedResidenceCommunity',
    'Gene',
    'GeneralContractor',
    'GeoCircle',
    'GeoCoordinates',
    'GeoShape',
    'GeospatialGeometry',
    'GiveAction',
    'GolfCourse',
    'GovernmentBuilding',
    'GovernmentOffice',
    'GovernmentOrganization',
    'GovernmentPermit',
    'GovernmentService',
    'Grant',
    'GroceryStore',
    'Guide',
    'HVACBusiness',
    'Hackathon',
    'HairSalon',
    'HardwareStore',
    'HealthAndBeautyBusiness',
    'HealthClub',
    'HealthInsurancePlan',
    'HealthPlanCostSharingSpecification',
    'HealthPlanFormulary',
    'HealthPlanNetwork',
    'HealthTopicContent',
    'HighSchool',
    'HinduTemple',
    'HobbyShop',
    'HomeAndConstructionBusiness',
    'HomeGoodsStore',
    'Hospital',
    'Hostel',
    'Hotel',
    'HotelRoom',
    'House',
    'HousePainter',
    'HowTo',
    'HowToDirection',
    'HowToItem',
    'HowToSection',
    'HowToStep',
    'HowToSupply',
    'HowToTip',
    'HowToTool',
    'HyperToc',
    'HyperTocEntry',
    'IceCreamShop',
    'IgnoreAction',
    'ImageGallery',
    'ImageObject',
    'ImageObjectSnapshot',
    'ImagingTest',
    'IndividualPhysician',
    'IndividualProduct',
    'InfectiousDisease',
    'InformAction',
    'InsertAction',
    'InstallAction',
    'InstantaneousEvent',
    'InsuranceAgency',
    'Intangible',
    'InteractAction',
    'InteractionCounter',
    'InternetCafe',
    'InvestmentFund',
    'InvestmentOrDeposit',
    'InviteAction',
    'Invoice',
    'ItemList',
    'ItemPage',
    'JewelryStore',
    'JobPosting',
    'JoinAction',
    'Joint',
    'LakeBodyOfWater',
    'Landform',
    'LandmarksOrHistoricalBuildings',
    'Language',
    'LearningResource',
    'LeaveAction',
    'LegalService',
    'Legislation',
    'LegislationObject',
    'LegislativeBuilding',
    'LendAction',
    'Library',
    'LibrarySystem',
    'LifestyleModification',
    'Ligament',
    'LikeAction',
    'LinkRole',
    'LiquorStore',
    'ListItem',
    'ListenAction',
    'LiteraryEvent',
    'LiveBlogPosting',
    'LoanOrCredit',
    'LocalBusiness',
    'LocationFeatureSpecification',
    'Locksmith',
    'LodgingBusiness',
    'LodgingReservation',
    'LoginAction',
    'LoseAction',
    'LymphaticVessel',
    'Manuscript',
    'Map',
    'MarryAction',
    'MathSolver',
    'MaximumDoseSchedule',
    'MediaGallery',
    'MediaObject',
    'MediaReview',
    'MediaReviewItem',
    'MediaSubscription',
    'MedicalAudience',
    'MedicalBusiness',
    'MedicalCause',
    'MedicalClinic',
    'MedicalCode',
    'MedicalCondition',
    'MedicalConditionStage',
    'MedicalContraindication',
    'MedicalDevice',
    'MedicalEntity',
    'MedicalGuideline',
    'MedicalGuidelineContraindication',
    'MedicalGuidelineRecommendation',
    'MedicalIndication',
    'MedicalIntangible',
    'MedicalObservationalStudy',
    'MedicalOrganization',
    'MedicalProcedure',
    'MedicalRiskCalculator',
    'MedicalRiskEstimator',
    'MedicalRiskFactor',
    'MedicalRiskScore',
    'MedicalScholarlyArticle',
    'MedicalSign',
    'MedicalSignOrSymptom',
    'MedicalStudy',
    'MedicalSymptom',
    'MedicalTest',
    'MedicalTestPanel',
    'MedicalTherapy',
    'MedicalTrial',
    'MedicalWebPage',
    'MeetingRoom',
    'MemberProgram',
    'MemberProgramTier',
    'MensClothingStore',
    'Menu',
    'MenuItem',
    'MenuSection',
    'MerchantReturnPolicy',
    'MerchantReturnPolicySeasonalOverride',
    'Message',
    'MiddleSchool',
    'MobileApplication',
    'MobilePhoneStore',
    'MolecularEntity',
    'MonetaryAmount',
    'MonetaryAmountDistribution',
    'MonetaryGrant',
    'MoneyTransfer',
    'MortgageLoan',
    'Mosque',
    'Motel',
    'Motorcycle',
    'MotorcycleDealer',
    'MotorcycleRepair',
    'MotorizedBicycle',
    'Mountain',
    'MoveAction',
    'Movie',
    'MovieClip',
    'MovieRentalStore',
    'MovieSeries',
    'MovieTheater',
    'MovingCompany',
    'Muscle',
    'Museum',
    'MusicAlbum',
    'MusicComposition',
    'MusicEvent',
    'MusicGroup',
    'MusicPlaylist',
    'MusicRecording',
    'MusicRelease',
    'MusicStore',
    'MusicVenue',
    'MusicVideoObject',
    'NGO',
    'NailSalon',
    'Nerve',
    'NewsArticle',
    'NewsMediaOrganization',
    'Newspaper',
    'NightClub',
    'Notary',
    'NoteDigitalDocument',
    'NutritionInformation',
    'Observation',
    'Occupation',
    'OccupationalExperienceRequirements',
    'OccupationalTherapy',
    'OceanBodyOfWater',
    'Offer',
    'OfferCatalog',
    'OfferForLease',
    'OfferForPurchase',
    'OfferShippingDetails',
    'OfficeEquipmentStore',
    'OnDemandEvent',
    'OnlineBusiness',
    'OnlineMarketplace',
    'OnlineStore',
    'OpeningHoursSpecification',
    'OperatingSystem',
    'OpinionNewsArticle',
    'Optician',
    'Order',
    'OrderAction',
    'OrderItem',
    'Organization',
    'OrganizationRole',
    'OrganizeAction',
    'OutletStore',
    'OwnershipInfo',
    'PaintAction',
    'Painting',
    'PalliativeProcedure',
    'ParcelDelivery',
    'ParentAudience',
    'Park',
    'ParkingFacility',
    'PathologyTest',
    'Patient',
    'PawnShop',
    'PayAction',
    'PaymentCard',
    'PaymentChargeSpecification',
    'PaymentMethod',
    'PaymentService',
    'PeopleAudience',
    'PerformAction',
    'PerformanceRole',
    'PerformingArtsEvent',
    'PerformingArtsTheater',
    'PerformingGroup',
    'Periodical',
    'Permit',
    'Person',
    'PetStore',
    'Pharmacy',
    'Photograph',
    'PhotographAction',
    'PhysicalActivity',
    'PhysicalTherapy',
    'Physician',
    'PhysiciansOffice',
    'Place',
    'PlaceOfWorship',
    'PlanAction',
    'Play',
    'PlayAction',
    'PlayGameAction',
    'Playground',
    'Plumber',
    'PodcastEpisode',
    'PodcastSeason',
    'PodcastSeries',
    'PoliceStation',
    'PoliticalParty',
    'Pond',
    'PostOffice',
    'PostalAddress',
    'PostalCodeRangeSpecification',
    'Poster',
    'PreOrderAction',
    'PrependAction',
    'Preschool',
    'PresentationDigitalDocument',
    'PreventionIndication',
    'PriceSpecification',
    'Product',
    'ProductCollection',
    'ProductGroup',
    'ProductModel',
    'ProductReturnPolicy',
    'ProfessionalService',
    'ProfilePage',
    'ProgramMembership',
    'Project',
    'Property',
    'PropertyValue',
    'PropertyValueSpecification',
    'Protein',
    'PsychologicalTreatment',
    'PublicSwimmingPool',
    'PublicToilet',
    'PublicationEvent',
    'PublicationIssue',
    'PublicationVolume',
    'QAPage',
    'QuantitativeValue',
    'QuantitativeValueDistribution',
    'Question',
    'Quiz',
    'Quotation',
    'QuoteAction',
    'RVPark',
    'RadiationTherapy',
    'RadioBroadcastService',
    'RadioChannel',
    'RadioClip',
    'RadioEpisode',
    'RadioSeason',
    'RadioSeries',
    'RadioStation',
    'Rating',
    'ReactAction',
    'ReadAction',
    'RealEstateAgent',
    'RealEstateListing',
    'ReceiveAction',
    'Recipe',
    'Recommendation',
    'RecommendedDoseSchedule',
    'RecyclingCenter',
    'RegisterAction',
    'RejectAction',
    'RentAction',
    'RentalCarReservation',
    'RepaymentSpecification',
    'ReplaceAction',
    'ReplyAction',
    'Report',
    'ReportageNewsArticle',
    'ReportedDoseSchedule',
    'ResearchOrganization',
    'ResearchProject',
    'Researcher',
    'Reservation',
    'ReservationPackage',
    'ReserveAction',
    'Reservoir',
    'ResetPasswordAction',
    'Residence',
    'Resort',
    'Restaurant',
    'ResumeAction',
    'ReturnAction',
    'Review',
    'ReviewAction',
    'ReviewNewsArticle',
    'RiverBodyOfWater',
    'Role',
    'RoofingContractor',
    'Room',
    'RsvpAction',
    'RuntimePlatform',
    'SaleEvent',
    'SatiricalArticle',
    'Schedule',
    'ScheduleAction',
    'ScholarlyArticle',
    'School',
    'SchoolDistrict',
    'ScreeningEvent',
    'Sculpture',
    'SeaBodyOfWater',
    'SearchAction',
    'SearchRescueOrganization',
    'SearchResultsPage',
    'Season',
    'Seat',
    'SeekToAction',
    'SelfStorage',
    'SellAction',
    'SendAction',
    'SequentialArt',
    'Series',
    'Service',
    'ServiceChannel',
    'ServicePeriod',
    'ShareAction',
    'SheetMusic',
    'ShippingConditions',
    'ShippingDeliveryTime',
    'ShippingRateSettings',
    'ShippingService',
    'ShoeStore',
    'ShoppingCenter',
    'ShortStory',
    'SingleFamilyResidence',
    'SiteNavigationElement',
    'SkiResort',
    'SocialEvent',
    'SocialMediaPosting',
    'SoftwareApplication',
    'SoftwareSourceCode',
    'SolveMathAction',
    'SomeProducts',
    'SpeakableSpecification',
    'SpecialAnnouncement',
    'SportingGoodsStore',
    'SportsActivityLocation',
    'SportsClub',
    'SportsEvent',
    'SportsOrganization',
    'SportsTeam',
    'SpreadsheetDigitalDocument',
    'StadiumOrArena',
    'State',
    'Statement',
    'StatisticalPopulation',
    'StatisticalVariable',
    'Store',
    'StructuredValue',
    'StupidType',
    'SubscribeAction',
    'Substance',
    'SubwayStation',
    'Suite',
    'SuperficialAnatomy',
    'SurgicalProcedure',
    'SuspendAction',
    'Syllabus',
    'Synagogue',
    'TVClip',
    'TVEpisode',
    'TVSeason',
    'TVSeries',
    'Table',
    'TakeAction',
    'TattooParlor',
    'Taxi',
    'TaxiReservation',
    'TaxiService',
    'TaxiStand',
    'Taxon',
    'TechArticle',
    'TelevisionChannel',
    'TelevisionStation',
    'TennisComplex',
    'TextDigitalDocument',
    'TextObject',
    'TheaterEvent',
    'TheaterGroup',
    'TherapeuticProcedure',
    'Thesis',
    'Thing',
    'Ticket',
    'TieAction',
    'TipAction',
    'TireShop',
    'TouristAttraction',
    'TouristDestination',
    'TouristInformationCenter',
    'TouristTrip',
    'ToyStore',
    'TrackAction',
    'TradeAction',
    'TrainReservation',
    'TrainStation',
    'TrainTrip',
    'TransferAction',
    'TravelAction',
    'TravelAgency',
    'TreatmentIndication',
    'Trip',
    'TypeAndQuantityNode',
    'UnRegisterAction',
    'UnitPriceSpecification',
    'UpdateAction',
    'UseAction',
    'UserBlocks',
    'UserCheckins',
    'UserComments',
    'UserDownloads',
    'UserInteraction',
    'UserLikes',
    'UserPageVisits',
    'UserPlays',
    'UserPlusOnes',
    'UserReview',
    'UserTweets',
    'VacationRental',
    'Vehicle',
    'Vein',
    'Vessel',
    'VeterinaryCare',
    'VideoGallery',
    'VideoGame',
    'VideoGameClip',
    'VideoGameSeries',
    'VideoObject',
    'VideoObjectSnapshot',
    'ViewAction',
    'VirtualLocation',
    'VisualArtsEvent',
    'VisualArtwork',
    'VitalSign',
    'Volcano',
    'VoteAction',
    'WPAdBlock',
    'WPFooter',
    'WPHeader',
    'WPSideBar',
    'WantAction',
    'WarrantyPromise',
    'WatchAction',
    'Waterfall',
    'WearAction',
    'WebAPI',
    'WebApplication',
    'WebContent',
    'WebPage',
    'WebPageElement',
    'WebSite',
    'WholesaleStore',
    'WinAction',
    'Winery',
    'WorkBasedProgram',
    'WorkersUnion',
    'WriteAction',
    'Zoo',
    'ActionStatusType',
    'AdultOrientedEnumeration',
    'BedType',
    'BoardingPolicyType',
    'BodyMeasurementTypeEnumeration',
    'BookFormatType',
    'BusinessEntityType',
    'BusinessFunction',
    'CarUsageType',
    'CertificationStatusEnumeration',
    'ContactPointOption',
    'DENonprofitType',
    'DayOfWeek',
    'DeliveryMethod',
    'DigitalDocumentPermissionType',
    'DigitalPlatformEnumeration',
    'DriveWheelConfigurationValue',
    'DrugCostCategory',
    'DrugPregnancyCategory',
    'DrugPrescriptionStatus',
    'EUEnergyEfficiencyEnumeration',
    'EnergyEfficiencyEnumeration',
    'EnergyStarEnergyEfficiencyEnumeration',
    'Enumeration',
    'EventAttendanceModeEnumeration',
    'EventStatusType',
    'FulfillmentTypeEnumeration',
    'GameAvailabilityEnumeration',
    'GamePlayMode',
    'GameServerStatus',
    'GenderType',
    'GovernmentBenefitsType',
    'HealthAspectEnumeration',
    'IPTCDigitalSourceEnumeration',
    'ITNonprofitType',
    'IncentiveQualifiedExpenseType',
    'IncentiveStatus',
    'IncentiveType',
    'InfectiousAgentClass',
    'ItemAvailability',
    'ItemListOrderType',
    'LegalForceStatus',
    'LegalValueLevel',
    'MapCategoryType',
    'MeasurementMethodEnum',
    'MeasurementTypeEnumeration',
    'MediaEnumeration',
    'MediaManipulationRatingEnumeration',
    'MedicalAudienceType',
    'MedicalDevicePurpose',
    'MedicalEnumeration',
    'MedicalEvidenceLevel',
    'MedicalImagingTechnique',
    'MedicalObservationalStudyDesign',
    'MedicalProcedureType',
    'MedicalSpecialty',
    'MedicalStudyStatus',
    'MedicalTrialDesign',
    'MedicineSystem',
    'MerchantReturnEnumeration',
    'MusicAlbumProductionType',
    'MusicAlbumReleaseType',
    'MusicReleaseFormatType',
    'NLNonprofitType',
    'NonprofitType',
    'OfferItemCondition',
    'OrderStatus',
    'PaymentMethodType',
    'PaymentStatusType',
    'PhysicalActivityCategory',
    'PhysicalExam',
    'PriceComponentTypeEnumeration',
    'PriceTypeEnumeration',
    'ProductReturnEnumeration',
    'PurchaseType',
    'QualitativeValue',
    'RefundTypeEnumeration',
    'ReservationStatusType',
    'RestrictedDiet',
    'ReturnFeesEnumeration',
    'ReturnLabelSourceEnumeration',
    'ReturnMethodEnumeration',
    'RsvpResponseType',
    'SizeGroupEnumeration',
    'SizeSpecification',
    'SizeSystemEnumeration',
    'Specialty',
    'StatusEnumeration',
    'SteeringPositionValue',
    'TierBenefitEnumeration',
    'UKNonprofitType',
    'USNonprofitType',
    'WarrantyScope',
    'WearableMeasurementTypeEnumeration',
    'WearableSizeGroupEnumeration',
    'WearableSizeSystemEnumeration',
    'SCHEMA_VERSION',
    'ClassMetadata',
    'EnumerationMemberMetadata',
    'SchemaMap',
    'SchemaModel',
    'SchemaEnum',
    'CircularReferenceError',
]
