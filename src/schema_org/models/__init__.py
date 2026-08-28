# Generated Python code is licensed under MIT.
# Schema.org descriptions are licensed under CC BY-SA 3.0.
# See LICENSE-SCHEMA-ORG.txt.

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .three_d_model import ThreeDModel
    from .am_radio_channel import AMRadioChannel
    from .api_reference import APIReference
    from .about_page import AboutPage
    from .accept_action import AcceptAction
    from .accommodation import Accommodation
    from .accounting_service import AccountingService
    from .achieve_action import AchieveAction
    from .action import Action
    from .action_access_specification import ActionAccessSpecification
    from .activate_action import ActivateAction
    from .add_action import AddAction
    from .administrative_area import AdministrativeArea
    from .adult_entertainment import AdultEntertainment
    from .advertiser_content_article import AdvertiserContentArticle
    from .aggregate_offer import AggregateOffer
    from .aggregate_rating import AggregateRating
    from .agree_action import AgreeAction
    from .airline import Airline
    from .airport import Airport
    from .alignment_object import AlignmentObject
    from .allocate_action import AllocateAction
    from .amp_story import AmpStory
    from .amusement_park import AmusementPark
    from .analysis_news_article import AnalysisNewsArticle
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem
    from .animal_shelter import AnimalShelter
    from .answer import Answer
    from .apartment import Apartment
    from .apartment_complex import ApartmentComplex
    from .append_action import AppendAction
    from .apply_action import ApplyAction
    from .approved_indication import ApprovedIndication
    from .aquarium import Aquarium
    from .archive_component import ArchiveComponent
    from .archive_organization import ArchiveOrganization
    from .arrive_action import ArriveAction
    from .art_gallery import ArtGallery
    from .artery import Artery
    from .article import Article
    from .ask_action import AskAction
    from .ask_public_news_article import AskPublicNewsArticle
    from .assess_action import AssessAction
    from .assign_action import AssignAction
    from .atlas import Atlas
    from .attorney import Attorney
    from .audience import Audience
    from .audio_object import AudioObject
    from .audio_object_snapshot import AudioObjectSnapshot
    from .audiobook import Audiobook
    from .authenticate_action import AuthenticateAction
    from .authorize_action import AuthorizeAction
    from .auto_body_shop import AutoBodyShop
    from .auto_dealer import AutoDealer
    from .auto_parts_store import AutoPartsStore
    from .auto_rental import AutoRental
    from .auto_repair import AutoRepair
    from .auto_wash import AutoWash
    from .automated_teller import AutomatedTeller
    from .automotive_business import AutomotiveBusiness
    from .background_news_article import BackgroundNewsArticle
    from .bakery import Bakery
    from .bank_account import BankAccount
    from .bank_or_credit_union import BankOrCreditUnion
    from .bar_or_pub import BarOrPub
    from .barcode import Barcode
    from .beach import Beach
    from .beauty_salon import BeautySalon
    from .bed_and_breakfast import BedAndBreakfast
    from .bed_details import BedDetails
    from .befriend_action import BefriendAction
    from .bike_store import BikeStore
    from .bio_chem_entity import BioChemEntity
    from .blog import Blog
    from .blog_posting import BlogPosting
    from .blood_test import BloodTest
    from .boat_reservation import BoatReservation
    from .boat_terminal import BoatTerminal
    from .boat_trip import BoatTrip
    from .body_of_water import BodyOfWater
    from .bone import Bone
    from .book import Book
    from .book_series import BookSeries
    from .book_store import BookStore
    from .bookmark_action import BookmarkAction
    from .borrow_action import BorrowAction
    from .bowling_alley import BowlingAlley
    from .brain_structure import BrainStructure
    from .brand import Brand
    from .breadcrumb_list import BreadcrumbList
    from .brewery import Brewery
    from .bridge import Bridge
    from .broadcast_channel import BroadcastChannel
    from .broadcast_event import BroadcastEvent
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .broadcast_service import BroadcastService
    from .brokerage_account import BrokerageAccount
    from .buddhist_temple import BuddhistTemple
    from .bus_or_coach import BusOrCoach
    from .bus_reservation import BusReservation
    from .bus_station import BusStation
    from .bus_stop import BusStop
    from .bus_trip import BusTrip
    from .business_audience import BusinessAudience
    from .business_event import BusinessEvent
    from .buy_action import BuyAction
    from .cdcpmd_record import CDCPMDRecord
    from .cable_or_satellite_service import CableOrSatelliteService
    from .cafe_or_coffee_shop import CafeOrCoffeeShop
    from .campground import Campground
    from .camping_pitch import CampingPitch
    from .canal import Canal
    from .cancel_action import CancelAction
    from .car import Car
    from .casino import Casino
    from .category_code import CategoryCode
    from .category_code_set import CategoryCodeSet
    from .catholic_church import CatholicChurch
    from .cemetery import Cemetery
    from .certification import Certification
    from .chapter import Chapter
    from .check_action import CheckAction
    from .check_in_action import CheckInAction
    from .check_out_action import CheckOutAction
    from .checkout_page import CheckoutPage
    from .chemical_substance import ChemicalSubstance
    from .child_care import ChildCare
    from .childrens_event import ChildrensEvent
    from .choose_action import ChooseAction
    from .church import Church
    from .city import City
    from .city_hall import CityHall
    from .civic_structure import CivicStructure
    from .claim import Claim
    from .claim_review import ClaimReview
    from .class_ import Class
    from .clip import Clip
    from .clothing_store import ClothingStore
    from .code import Code
    from .collection import Collection
    from .collection_page import CollectionPage
    from .college_or_university import CollegeOrUniversity
    from .comedy_club import ComedyClub
    from .comedy_event import ComedyEvent
    from .comic_cover_art import ComicCoverArt
    from .comic_issue import ComicIssue
    from .comic_series import ComicSeries
    from .comic_story import ComicStory
    from .comment import Comment
    from .comment_action import CommentAction
    from .communicate_action import CommunicateAction
    from .complete_data_feed import CompleteDataFeed
    from .compound_price_specification import CompoundPriceSpecification
    from .computer_language import ComputerLanguage
    from .computer_store import ComputerStore
    from .conference_event import ConferenceEvent
    from .confirm_action import ConfirmAction
    from .consortium import Consortium
    from .constraint_node import ConstraintNode
    from .consume_action import ConsumeAction
    from .contact_page import ContactPage
    from .contact_point import ContactPoint
    from .continent import Continent
    from .control_action import ControlAction
    from .convenience_store import ConvenienceStore
    from .conversation import Conversation
    from .cook_action import CookAction
    from .cooperative import Cooperative
    from .corporation import Corporation
    from .correction_comment import CorrectionComment
    from .country import Country
    from .course import Course
    from .course_instance import CourseInstance
    from .courthouse import Courthouse
    from .cover_art import CoverArt
    from .covid_testing_facility import CovidTestingFacility
    from .create_action import CreateAction
    from .creative_work import CreativeWork
    from .creative_work_season import CreativeWorkSeason
    from .creative_work_series import CreativeWorkSeries
    from .credential import Credential
    from .credit_card import CreditCard
    from .crematorium import Crematorium
    from .critic_review import CriticReview
    from .currency_conversion_service import CurrencyConversionService
    from .d_dx_element import DDxElement
    from .dance_event import DanceEvent
    from .dance_group import DanceGroup
    from .data_catalog import DataCatalog
    from .data_download import DataDownload
    from .data_feed import DataFeed
    from .data_feed_item import DataFeedItem
    from .dataset import Dataset
    from .dated_money_specification import DatedMoneySpecification
    from .day_spa import DaySpa
    from .deactivate_action import DeactivateAction
    from .defence_establishment import DefenceEstablishment
    from .defined_region import DefinedRegion
    from .defined_term import DefinedTerm
    from .defined_term_set import DefinedTermSet
    from .delete_action import DeleteAction
    from .delivery_charge_specification import DeliveryChargeSpecification
    from .delivery_event import DeliveryEvent
    from .delivery_time_settings import DeliveryTimeSettings
    from .demand import Demand
    from .dentist import Dentist
    from .depart_action import DepartAction
    from .department_store import DepartmentStore
    from .deposit_account import DepositAccount
    from .diagnostic_lab import DiagnosticLab
    from .diagnostic_procedure import DiagnosticProcedure
    from .diet import Diet
    from .dietary_supplement import DietarySupplement
    from .digital_document import DigitalDocument
    from .digital_document_permission import DigitalDocumentPermission
    from .disagree_action import DisagreeAction
    from .discover_action import DiscoverAction
    from .discussion_forum_posting import DiscussionForumPosting
    from .dislike_action import DislikeAction
    from .distillery import Distillery
    from .donate_action import DonateAction
    from .dose_schedule import DoseSchedule
    from .download_action import DownloadAction
    from .draw_action import DrawAction
    from .drawing import Drawing
    from .drink_action import DrinkAction
    from .drug import Drug
    from .drug_class import DrugClass
    from .drug_cost import DrugCost
    from .drug_legal_status import DrugLegalStatus
    from .drug_strength import DrugStrength
    from .dry_cleaning_or_laundry import DryCleaningOrLaundry
    from .eat_action import EatAction
    from .education_event import EducationEvent
    from .educational_audience import EducationalAudience
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .educational_occupational_program import EducationalOccupationalProgram
    from .educational_organization import EducationalOrganization
    from .electrician import Electrician
    from .electronics_store import ElectronicsStore
    from .elementary_school import ElementarySchool
    from .email_message import EmailMessage
    from .embassy import Embassy
    from .emergency_service import EmergencyService
    from .employee_role import EmployeeRole
    from .employer_aggregate_rating import EmployerAggregateRating
    from .employer_review import EmployerReview
    from .employment_agency import EmploymentAgency
    from .endorse_action import EndorseAction
    from .endorsement_rating import EndorsementRating
    from .energy_consumption_details import EnergyConsumptionDetails
    from .engine_specification import EngineSpecification
    from .entertainment_business import EntertainmentBusiness
    from .entry_point import EntryPoint
    from .episode import Episode
    from .error import Error
    from .event import Event
    from .event_reservation import EventReservation
    from .event_series import EventSeries
    from .event_venue import EventVenue
    from .exchange_rate_specification import ExchangeRateSpecification
    from .exercise_action import ExerciseAction
    from .exercise_gym import ExerciseGym
    from .exercise_plan import ExercisePlan
    from .exhibition_event import ExhibitionEvent
    from .faq_page import FAQPage
    from .fm_radio_channel import FMRadioChannel
    from .fast_food_restaurant import FastFoodRestaurant
    from .festival import Festival
    from .film_action import FilmAction
    from .financial_incentive import FinancialIncentive
    from .financial_product import FinancialProduct
    from .financial_service import FinancialService
    from .find_action import FindAction
    from .fire_station import FireStation
    from .flight import Flight
    from .flight_reservation import FlightReservation
    from .floor_plan import FloorPlan
    from .florist import Florist
    from .follow_action import FollowAction
    from .food_establishment import FoodEstablishment
    from .food_establishment_reservation import FoodEstablishmentReservation
    from .food_event import FoodEvent
    from .food_service import FoodService
    from .funding_agency import FundingAgency
    from .funding_scheme import FundingScheme
    from .furniture_store import FurnitureStore
    from .game import Game
    from .game_server import GameServer
    from .garden_store import GardenStore
    from .gas_station import GasStation
    from .gated_residence_community import GatedResidenceCommunity
    from .gene import Gene
    from .general_contractor import GeneralContractor
    from .geo_circle import GeoCircle
    from .geo_coordinates import GeoCoordinates
    from .geo_shape import GeoShape
    from .geospatial_geometry import GeospatialGeometry
    from .give_action import GiveAction
    from .golf_course import GolfCourse
    from .government_building import GovernmentBuilding
    from .government_office import GovernmentOffice
    from .government_organization import GovernmentOrganization
    from .government_permit import GovernmentPermit
    from .government_service import GovernmentService
    from .grant import Grant
    from .grocery_store import GroceryStore
    from .guide import Guide
    from .hvac_business import HVACBusiness
    from .hackathon import Hackathon
    from .hair_salon import HairSalon
    from .hardware_store import HardwareStore
    from .health_and_beauty_business import HealthAndBeautyBusiness
    from .health_club import HealthClub
    from .health_insurance_plan import HealthInsurancePlan
    from .health_plan_cost_sharing_specification import HealthPlanCostSharingSpecification
    from .health_plan_formulary import HealthPlanFormulary
    from .health_plan_network import HealthPlanNetwork
    from .health_topic_content import HealthTopicContent
    from .high_school import HighSchool
    from .hindu_temple import HinduTemple
    from .hobby_shop import HobbyShop
    from .home_and_construction_business import HomeAndConstructionBusiness
    from .home_goods_store import HomeGoodsStore
    from .hospital import Hospital
    from .hostel import Hostel
    from .hotel import Hotel
    from .hotel_room import HotelRoom
    from .house import House
    from .house_painter import HousePainter
    from .how_to import HowTo
    from .how_to_direction import HowToDirection
    from .how_to_item import HowToItem
    from .how_to_section import HowToSection
    from .how_to_step import HowToStep
    from .how_to_supply import HowToSupply
    from .how_to_tip import HowToTip
    from .how_to_tool import HowToTool
    from .hyper_toc import HyperToc
    from .hyper_toc_entry import HyperTocEntry
    from .ice_cream_shop import IceCreamShop
    from .ignore_action import IgnoreAction
    from .image_gallery import ImageGallery
    from .image_object import ImageObject
    from .image_object_snapshot import ImageObjectSnapshot
    from .imaging_test import ImagingTest
    from .individual_physician import IndividualPhysician
    from .individual_product import IndividualProduct
    from .infectious_disease import InfectiousDisease
    from .inform_action import InformAction
    from .insert_action import InsertAction
    from .install_action import InstallAction
    from .instantaneous_event import InstantaneousEvent
    from .insurance_agency import InsuranceAgency
    from .intangible import Intangible
    from .interact_action import InteractAction
    from .interaction_counter import InteractionCounter
    from .internet_cafe import InternetCafe
    from .investment_fund import InvestmentFund
    from .investment_or_deposit import InvestmentOrDeposit
    from .invite_action import InviteAction
    from .invoice import Invoice
    from .item_list import ItemList
    from .item_page import ItemPage
    from .jewelry_store import JewelryStore
    from .job_posting import JobPosting
    from .join_action import JoinAction
    from .joint import Joint
    from .lake_body_of_water import LakeBodyOfWater
    from .landform import Landform
    from .landmarks_or_historical_buildings import LandmarksOrHistoricalBuildings
    from .language import Language
    from .learning_resource import LearningResource
    from .leave_action import LeaveAction
    from .legal_service import LegalService
    from .legislation import Legislation
    from .legislation_object import LegislationObject
    from .legislative_building import LegislativeBuilding
    from .lend_action import LendAction
    from .library import Library
    from .library_system import LibrarySystem
    from .lifestyle_modification import LifestyleModification
    from .ligament import Ligament
    from .like_action import LikeAction
    from .link_role import LinkRole
    from .liquor_store import LiquorStore
    from .list_item import ListItem
    from .listen_action import ListenAction
    from .literary_event import LiteraryEvent
    from .live_blog_posting import LiveBlogPosting
    from .loan_or_credit import LoanOrCredit
    from .local_business import LocalBusiness
    from .location_feature_specification import LocationFeatureSpecification
    from .locksmith import Locksmith
    from .lodging_business import LodgingBusiness
    from .lodging_reservation import LodgingReservation
    from .login_action import LoginAction
    from .lose_action import LoseAction
    from .lymphatic_vessel import LymphaticVessel
    from .manuscript import Manuscript
    from .map import Map
    from .marry_action import MarryAction
    from .math_solver import MathSolver
    from .maximum_dose_schedule import MaximumDoseSchedule
    from .media_gallery import MediaGallery
    from .media_object import MediaObject
    from .media_review import MediaReview
    from .media_review_item import MediaReviewItem
    from .media_subscription import MediaSubscription
    from .medical_audience import MedicalAudience
    from .medical_business import MedicalBusiness
    from .medical_cause import MedicalCause
    from .medical_clinic import MedicalClinic
    from .medical_code import MedicalCode
    from .medical_condition import MedicalCondition
    from .medical_condition_stage import MedicalConditionStage
    from .medical_contraindication import MedicalContraindication
    from .medical_device import MedicalDevice
    from .medical_entity import MedicalEntity
    from .medical_guideline import MedicalGuideline
    from .medical_guideline_contraindication import MedicalGuidelineContraindication
    from .medical_guideline_recommendation import MedicalGuidelineRecommendation
    from .medical_indication import MedicalIndication
    from .medical_intangible import MedicalIntangible
    from .medical_observational_study import MedicalObservationalStudy
    from .medical_organization import MedicalOrganization
    from .medical_procedure import MedicalProcedure
    from .medical_risk_calculator import MedicalRiskCalculator
    from .medical_risk_estimator import MedicalRiskEstimator
    from .medical_risk_factor import MedicalRiskFactor
    from .medical_risk_score import MedicalRiskScore
    from .medical_scholarly_article import MedicalScholarlyArticle
    from .medical_sign import MedicalSign
    from .medical_sign_or_symptom import MedicalSignOrSymptom
    from .medical_study import MedicalStudy
    from .medical_symptom import MedicalSymptom
    from .medical_test import MedicalTest
    from .medical_test_panel import MedicalTestPanel
    from .medical_therapy import MedicalTherapy
    from .medical_trial import MedicalTrial
    from .medical_web_page import MedicalWebPage
    from .meeting_room import MeetingRoom
    from .member_program import MemberProgram
    from .member_program_tier import MemberProgramTier
    from .mens_clothing_store import MensClothingStore
    from .menu import Menu
    from .menu_item import MenuItem
    from .menu_section import MenuSection
    from .merchant_return_policy import MerchantReturnPolicy
    from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .message import Message
    from .middle_school import MiddleSchool
    from .mobile_application import MobileApplication
    from .mobile_phone_store import MobilePhoneStore
    from .molecular_entity import MolecularEntity
    from .monetary_amount import MonetaryAmount
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .monetary_grant import MonetaryGrant
    from .money_transfer import MoneyTransfer
    from .mortgage_loan import MortgageLoan
    from .mosque import Mosque
    from .motel import Motel
    from .motorcycle import Motorcycle
    from .motorcycle_dealer import MotorcycleDealer
    from .motorcycle_repair import MotorcycleRepair
    from .motorized_bicycle import MotorizedBicycle
    from .mountain import Mountain
    from .move_action import MoveAction
    from .movie import Movie
    from .movie_clip import MovieClip
    from .movie_rental_store import MovieRentalStore
    from .movie_series import MovieSeries
    from .movie_theater import MovieTheater
    from .moving_company import MovingCompany
    from .muscle import Muscle
    from .museum import Museum
    from .music_album import MusicAlbum
    from .music_composition import MusicComposition
    from .music_event import MusicEvent
    from .music_group import MusicGroup
    from .music_playlist import MusicPlaylist
    from .music_recording import MusicRecording
    from .music_release import MusicRelease
    from .music_store import MusicStore
    from .music_venue import MusicVenue
    from .music_video_object import MusicVideoObject
    from .ngo import NGO
    from .nail_salon import NailSalon
    from .nerve import Nerve
    from .news_article import NewsArticle
    from .news_media_organization import NewsMediaOrganization
    from .newspaper import Newspaper
    from .night_club import NightClub
    from .notary import Notary
    from .note_digital_document import NoteDigitalDocument
    from .nutrition_information import NutritionInformation
    from .observation import Observation
    from .occupation import Occupation
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .occupational_therapy import OccupationalTherapy
    from .ocean_body_of_water import OceanBodyOfWater
    from .offer import Offer
    from .offer_catalog import OfferCatalog
    from .offer_for_lease import OfferForLease
    from .offer_for_purchase import OfferForPurchase
    from .offer_shipping_details import OfferShippingDetails
    from .office_equipment_store import OfficeEquipmentStore
    from .on_demand_event import OnDemandEvent
    from .online_business import OnlineBusiness
    from .online_marketplace import OnlineMarketplace
    from .online_store import OnlineStore
    from .opening_hours_specification import OpeningHoursSpecification
    from .operating_system import OperatingSystem
    from .opinion_news_article import OpinionNewsArticle
    from .optician import Optician
    from .order import Order
    from .order_action import OrderAction
    from .order_item import OrderItem
    from .organization import Organization
    from .organization_role import OrganizationRole
    from .organize_action import OrganizeAction
    from .outlet_store import OutletStore
    from .ownership_info import OwnershipInfo
    from .paint_action import PaintAction
    from .painting import Painting
    from .palliative_procedure import PalliativeProcedure
    from .parcel_delivery import ParcelDelivery
    from .parent_audience import ParentAudience
    from .park import Park
    from .parking_facility import ParkingFacility
    from .pathology_test import PathologyTest
    from .patient import Patient
    from .pawn_shop import PawnShop
    from .pay_action import PayAction
    from .payment_card import PaymentCard
    from .payment_charge_specification import PaymentChargeSpecification
    from .payment_method import PaymentMethod
    from .payment_service import PaymentService
    from .people_audience import PeopleAudience
    from .perform_action import PerformAction
    from .performance_role import PerformanceRole
    from .performing_arts_event import PerformingArtsEvent
    from .performing_arts_theater import PerformingArtsTheater
    from .performing_group import PerformingGroup
    from .periodical import Periodical
    from .permit import Permit
    from .person import Person
    from .pet_store import PetStore
    from .pharmacy import Pharmacy
    from .photograph import Photograph
    from .photograph_action import PhotographAction
    from .physical_activity import PhysicalActivity
    from .physical_therapy import PhysicalTherapy
    from .physician import Physician
    from .physicians_office import PhysiciansOffice
    from .place import Place
    from .place_of_worship import PlaceOfWorship
    from .plan_action import PlanAction
    from .play import Play
    from .play_action import PlayAction
    from .play_game_action import PlayGameAction
    from .playground import Playground
    from .plumber import Plumber
    from .podcast_episode import PodcastEpisode
    from .podcast_season import PodcastSeason
    from .podcast_series import PodcastSeries
    from .police_station import PoliceStation
    from .political_party import PoliticalParty
    from .pond import Pond
    from .post_office import PostOffice
    from .postal_address import PostalAddress
    from .postal_code_range_specification import PostalCodeRangeSpecification
    from .poster import Poster
    from .pre_order_action import PreOrderAction
    from .prepend_action import PrependAction
    from .preschool import Preschool
    from .presentation_digital_document import PresentationDigitalDocument
    from .prevention_indication import PreventionIndication
    from .price_specification import PriceSpecification
    from .product import Product
    from .product_collection import ProductCollection
    from .product_group import ProductGroup
    from .product_model import ProductModel
    from .product_return_policy import ProductReturnPolicy
    from .professional_service import ProfessionalService
    from .profile_page import ProfilePage
    from .program_membership import ProgramMembership
    from .project import Project
    from .property import Property
    from .property_value import PropertyValue
    from .property_value_specification import PropertyValueSpecification
    from .protein import Protein
    from .psychological_treatment import PsychologicalTreatment
    from .public_swimming_pool import PublicSwimmingPool
    from .public_toilet import PublicToilet
    from .publication_event import PublicationEvent
    from .publication_issue import PublicationIssue
    from .publication_volume import PublicationVolume
    from .qa_page import QAPage
    from .quantitative_value import QuantitativeValue
    from .quantitative_value_distribution import QuantitativeValueDistribution
    from .question import Question
    from .quiz import Quiz
    from .quotation import Quotation
    from .quote_action import QuoteAction
    from .rv_park import RVPark
    from .radiation_therapy import RadiationTherapy
    from .radio_broadcast_service import RadioBroadcastService
    from .radio_channel import RadioChannel
    from .radio_clip import RadioClip
    from .radio_episode import RadioEpisode
    from .radio_season import RadioSeason
    from .radio_series import RadioSeries
    from .radio_station import RadioStation
    from .rating import Rating
    from .react_action import ReactAction
    from .read_action import ReadAction
    from .real_estate_agent import RealEstateAgent
    from .real_estate_listing import RealEstateListing
    from .receive_action import ReceiveAction
    from .recipe import Recipe
    from .recommendation import Recommendation
    from .recommended_dose_schedule import RecommendedDoseSchedule
    from .recycling_center import RecyclingCenter
    from .register_action import RegisterAction
    from .reject_action import RejectAction
    from .rent_action import RentAction
    from .rental_car_reservation import RentalCarReservation
    from .repayment_specification import RepaymentSpecification
    from .replace_action import ReplaceAction
    from .reply_action import ReplyAction
    from .report import Report
    from .reportage_news_article import ReportageNewsArticle
    from .reported_dose_schedule import ReportedDoseSchedule
    from .research_organization import ResearchOrganization
    from .research_project import ResearchProject
    from .researcher import Researcher
    from .reservation import Reservation
    from .reservation_package import ReservationPackage
    from .reserve_action import ReserveAction
    from .reservoir import Reservoir
    from .reset_password_action import ResetPasswordAction
    from .residence import Residence
    from .resort import Resort
    from .restaurant import Restaurant
    from .resume_action import ResumeAction
    from .return_action import ReturnAction
    from .review import Review
    from .review_action import ReviewAction
    from .review_news_article import ReviewNewsArticle
    from .river_body_of_water import RiverBodyOfWater
    from .role import Role
    from .roofing_contractor import RoofingContractor
    from .room import Room
    from .rsvp_action import RsvpAction
    from .runtime_platform import RuntimePlatform
    from .sale_event import SaleEvent
    from .satirical_article import SatiricalArticle
    from .schedule import Schedule
    from .schedule_action import ScheduleAction
    from .scholarly_article import ScholarlyArticle
    from .school import School
    from .school_district import SchoolDistrict
    from .screening_event import ScreeningEvent
    from .sculpture import Sculpture
    from .sea_body_of_water import SeaBodyOfWater
    from .search_action import SearchAction
    from .search_rescue_organization import SearchRescueOrganization
    from .search_results_page import SearchResultsPage
    from .season import Season
    from .seat import Seat
    from .seek_to_action import SeekToAction
    from .self_storage import SelfStorage
    from .sell_action import SellAction
    from .send_action import SendAction
    from .sequential_art import SequentialArt
    from .series import Series
    from .service import Service
    from .service_channel import ServiceChannel
    from .service_period import ServicePeriod
    from .share_action import ShareAction
    from .sheet_music import SheetMusic
    from .shipping_conditions import ShippingConditions
    from .shipping_delivery_time import ShippingDeliveryTime
    from .shipping_rate_settings import ShippingRateSettings
    from .shipping_service import ShippingService
    from .shoe_store import ShoeStore
    from .shopping_center import ShoppingCenter
    from .short_story import ShortStory
    from .single_family_residence import SingleFamilyResidence
    from .site_navigation_element import SiteNavigationElement
    from .ski_resort import SkiResort
    from .social_event import SocialEvent
    from .social_media_posting import SocialMediaPosting
    from .software_application import SoftwareApplication
    from .software_source_code import SoftwareSourceCode
    from .solve_math_action import SolveMathAction
    from .some_products import SomeProducts
    from .speakable_specification import SpeakableSpecification
    from .special_announcement import SpecialAnnouncement
    from .sporting_goods_store import SportingGoodsStore
    from .sports_activity_location import SportsActivityLocation
    from .sports_club import SportsClub
    from .sports_event import SportsEvent
    from .sports_organization import SportsOrganization
    from .sports_team import SportsTeam
    from .spreadsheet_digital_document import SpreadsheetDigitalDocument
    from .stadium_or_arena import StadiumOrArena
    from .state import State
    from .statement import Statement
    from .statistical_population import StatisticalPopulation
    from .statistical_variable import StatisticalVariable
    from .store import Store
    from .structured_value import StructuredValue
    from .stupid_type import StupidType
    from .subscribe_action import SubscribeAction
    from .substance import Substance
    from .subway_station import SubwayStation
    from .suite import Suite
    from .superficial_anatomy import SuperficialAnatomy
    from .surgical_procedure import SurgicalProcedure
    from .suspend_action import SuspendAction
    from .syllabus import Syllabus
    from .synagogue import Synagogue
    from .tv_clip import TVClip
    from .tv_episode import TVEpisode
    from .tv_season import TVSeason
    from .tv_series import TVSeries
    from .table import Table
    from .take_action import TakeAction
    from .tattoo_parlor import TattooParlor
    from .taxi import Taxi
    from .taxi_reservation import TaxiReservation
    from .taxi_service import TaxiService
    from .taxi_stand import TaxiStand
    from .taxon import Taxon
    from .tech_article import TechArticle
    from .television_channel import TelevisionChannel
    from .television_station import TelevisionStation
    from .tennis_complex import TennisComplex
    from .text_digital_document import TextDigitalDocument
    from .text_object import TextObject
    from .theater_event import TheaterEvent
    from .theater_group import TheaterGroup
    from .therapeutic_procedure import TherapeuticProcedure
    from .thesis import Thesis
    from .thing import Thing
    from .ticket import Ticket
    from .tie_action import TieAction
    from .tip_action import TipAction
    from .tire_shop import TireShop
    from .tourist_attraction import TouristAttraction
    from .tourist_destination import TouristDestination
    from .tourist_information_center import TouristInformationCenter
    from .tourist_trip import TouristTrip
    from .toy_store import ToyStore
    from .track_action import TrackAction
    from .trade_action import TradeAction
    from .train_reservation import TrainReservation
    from .train_station import TrainStation
    from .train_trip import TrainTrip
    from .transfer_action import TransferAction
    from .travel_action import TravelAction
    from .travel_agency import TravelAgency
    from .treatment_indication import TreatmentIndication
    from .trip import Trip
    from .type_and_quantity_node import TypeAndQuantityNode
    from .un_register_action import UnRegisterAction
    from .unit_price_specification import UnitPriceSpecification
    from .update_action import UpdateAction
    from .use_action import UseAction
    from .user_blocks import UserBlocks
    from .user_checkins import UserCheckins
    from .user_comments import UserComments
    from .user_downloads import UserDownloads
    from .user_interaction import UserInteraction
    from .user_likes import UserLikes
    from .user_page_visits import UserPageVisits
    from .user_plays import UserPlays
    from .user_plus_ones import UserPlusOnes
    from .user_review import UserReview
    from .user_tweets import UserTweets
    from .vacation_rental import VacationRental
    from .vehicle import Vehicle
    from .vein import Vein
    from .vessel import Vessel
    from .veterinary_care import VeterinaryCare
    from .video_gallery import VideoGallery
    from .video_game import VideoGame
    from .video_game_clip import VideoGameClip
    from .video_game_series import VideoGameSeries
    from .video_object import VideoObject
    from .video_object_snapshot import VideoObjectSnapshot
    from .view_action import ViewAction
    from .virtual_location import VirtualLocation
    from .visual_arts_event import VisualArtsEvent
    from .visual_artwork import VisualArtwork
    from .vital_sign import VitalSign
    from .volcano import Volcano
    from .vote_action import VoteAction
    from .wp_ad_block import WPAdBlock
    from .wp_footer import WPFooter
    from .wp_header import WPHeader
    from .wp_side_bar import WPSideBar
    from .want_action import WantAction
    from .warranty_promise import WarrantyPromise
    from .watch_action import WatchAction
    from .waterfall import Waterfall
    from .wear_action import WearAction
    from .web_api import WebAPI
    from .web_application import WebApplication
    from .web_content import WebContent
    from .web_page import WebPage
    from .web_page_element import WebPageElement
    from .web_site import WebSite
    from .wholesale_store import WholesaleStore
    from .win_action import WinAction
    from .winery import Winery
    from .work_based_program import WorkBasedProgram
    from .workers_union import WorkersUnion
    from .write_action import WriteAction
    from .zoo import Zoo

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

def __getattr__(name: str):
    module_name = _MODEL_MODULES.get(name)
    if module_name is None:
        raise AttributeError(name)
    return getattr(import_module(f'.{module_name}', __name__), name)

def __dir__():
    return sorted(set(globals()) | set(_MODEL_MODULES))
