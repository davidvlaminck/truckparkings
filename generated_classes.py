import abc
import datetime
from enum import Enum
import xml.etree.ElementTree as ET


class ServiceFacilityTypeEnum(str, Enum):
    Hotel = 'hotel'
    Motel = 'motel'
    OvernightAccommodation = 'overnightAccommodation'
    Shop = 'shop'
    Kiosk = 'kiosk'
    FoodShopping = 'foodShopping'
    Cafe = 'cafe'
    Restaurant = 'restaurant'
    RestaurantSelfService = 'restaurantSelfService'
    MotorwayRestaurant = 'motorwayRestaurant'
    MotorwayRestaurantSmall = 'motorwayRestaurantSmall'
    SparePartsShopping = 'sparePartsShopping'
    PetrolStation = 'petrolStation'
    VehicleMaintenance = 'vehicleMaintenance'
    TyreRepair = 'tyreRepair'
    TruckRepair = 'truckRepair'
    TruckWash = 'truckWash'
    CarWash = 'carWash'
    Pharmacy = 'pharmacy'
    MedicalFacility = 'medicalFacility'
    Police = 'police'
    TouristInformation = 'touristInformation'
    BikeSharing = 'bikeSharing'
    Docstop = 'docstop'
    Laundry = 'laundry'
    LeisureActivities = 'leisureActivities'
    Unknown = 'unknown'
    Other = 'other'


class CountryEnum(str, Enum):
    """CountryEnum -- List of countries.

    """
    AT = 'at'  # Austria
    BE = 'be'  # Belgium
    BG = 'bg'  # Bulgaria
    CH = 'ch'  # Switzerland
    CS = 'cs'  # Serbia and Montenegro
    CY = 'cy'  # Cyprus
    CZ = 'cz'  # Czech Republic
    DE = 'de'  # Germany
    DK = 'dk'  # Denmark
    EE = 'ee'  # Estonia
    ES = 'es'  # Spain
    FI = 'fi'  # Finland
    FO = 'fo'  # Faroe Islands
    FR = 'fr'  # France
    GB = 'gb'  # Great Britain
    GG = 'gg'  # Guernsey
    GI = 'gi'  # Gibraltar
    GR = 'gr'  # Greece
    HR = 'hr'  # Croatia
    HU = 'hu'  # Hungary
    IE = 'ie'  # Ireland
    IM = 'im'  # Isle Of Man
    IS = 'is'  # Iceland
    IT = 'it'  # Italy
    JE = 'je'  # Jersey
    LI = 'li'  # Lichtenstein
    LT = 'lt'  # Lithuania
    LU = 'lu'  # Luxembourg
    LV = 'lv'  # Latvia
    MA = 'ma'  # Morocco
    MC = 'mc'  # Monaco
    MK = 'mk'  # Macedonia
    MT = 'mt'  # Malta
    NL = 'nl'  # Netherlands
    NO = 'no'  # Norway
    PL = 'pl'  # Poland
    PT = 'pt'  # Portugal
    RO = 'ro'  # Romania
    SE = 'se'  # Sweden
    SI = 'si'  # Slovenia
    SK = 'sk'  # Slovakia
    SM = 'sm'  # San Marino
    TR = 'tr'  # Turkey
    VA = 'va'  # Vatican City State
    OTHER = 'other'  # Other than as defined in this enumeration.


def validate_countryEnum(country) -> bool:
    if country not in CountryEnum:
        raise ValueError(f'Invalid country: {country}')
    return True


def validate_serviceFacilityTypeEnum(serviceFacilityType) -> bool:
    if serviceFacilityType not in ServiceFacilityTypeEnum:
        raise ValueError(f'Invalid ServiceFacilityType: {serviceFacilityType}')
    return True

class GeneratedClass(abc.ABC):
    @abc.abstractmethod
    def to_element(self, parent: ET.Element):
        raise NotImplementedError

    def __init__(self):
        self._name = None
        self._attributes = None


class BaseGeneratedClass(GeneratedClass):
    def __init__(self, content: object):
        super().__init__()
        self.content = content

    def to_element(self, parent: ET.Element):
        if self._attributes is None:
            el = ET.SubElement(parent, self._name)
        else:
            el = ET.SubElement(parent, self._name, attrib=self._attributes)
        el.text = self.content


class GeneratedIndexedListClassWithChildren(GeneratedClass):
    def __init__(self, children: list, index_name: str = 'index'):
        super().__init__()
        self._index_name = index_name
        self._children = children

    def to_element(self, parent: ET.Element):
        for index, child in enumerate(c for c in self._children if c is not None):
            if child._attributes is None:
                child._attributes = {}
            child._attributes[self._index_name] = str(index)
            child.to_element(parent=parent)


class GeneratedClassWithChildren(GeneratedClass):
    def __init__(self, children):
        super().__init__()
        self._children = children

    def to_element(self, parent: ET.Element):
        if self._attributes is None:
            el = ET.SubElement(parent, self._name)
        else:
            el = ET.SubElement(parent, self._name, attrib=self._attributes)

        for child in (c for c in self._children if c is not None):
            child.to_element(parent=el)


class NationalIdentifier(BaseGeneratedClass):
    """NationalIdentifier -- An identifier/name unique within the specified country."""

    def __init__(self, content: str):
        super().__init__(content)
        self._name = 'nationalIdentifier'


class Country(BaseGeneratedClass):
    """Country -- A country."""

    def __init__(self, content: str):
        validate_countryEnum(content)
        super().__init__(content)
        self._name = 'country'


class InternationalIdentifier(GeneratedClassWithChildren):
    """InternationalIdentifier -- An identifier/name whose range is specific to the particular country.
    country -- ISO 3166-1 two character country code.
    nationalIdentifier -- Identifier or name unique within the specified country.
    """

    def __init__(self, country: Country, nationalIdentifier: NationalIdentifier,
                 internationalIdentifierExtension=None, name: str = None):
        super().__init__((country, nationalIdentifier, internationalIdentifierExtension))
        self._name = name


class Exchange(GeneratedClassWithChildren):
    """Exchange -- Details associated with the management of the exchange between the supplier and the client."""

    def __init__(self, supplierIdentification: InternationalIdentifier = None, exchangeExtension=None):
        supplierIdentification._name = 'supplierIdentification'
        super().__init__((supplierIdentification, exchangeExtension))
        self._name = 'exchange'


class PublicationCreator(GeneratedClassWithChildren):
    """PublicationCreator -- Details of the creator of the DATEX II publication.
    """

    def __init__(self, publicationCreator: InternationalIdentifier = None):
        super().__init__((publicationCreator,))
        self._name = 'publicationCreator'


class GenericPublicationName(BaseGeneratedClass):
    """GenericPublicationName -- The name of the generic publication."""

    def __init__(self, content: str):
        super().__init__(content)
        self._name = 'genericPublicationName'


class ParkingRecordVersionTime(BaseGeneratedClass):
    """Date/time that this version of the parking record was defined."""

    def __init__(self):
        super().__init__(datetime.datetime.now().astimezone().isoformat())
        self._name = 'parkingRecordVersionTime'


class ParkingTableVersionTime(BaseGeneratedClass):
    """The date/time that this version of the parking table was defined by the supplier. The identity and version
    of the table are defined by the class stereotype implementation."""

    def __init__(self):
        super().__init__(datetime.datetime.now().astimezone().isoformat())
        self._name = 'parkingTableVersionTime'


class PublicationTime(BaseGeneratedClass):
    def __init__(self):
        super().__init__("")
        self._name = 'publicationTime'
        self.content = datetime.datetime.now().astimezone().isoformat()


class MultilingualStringValue(BaseGeneratedClass):
    """MultilingualStringValue -- A string of characters expressed in a single language.
    lang -- The language of the text.
    value -- The text string.
    """

    def __init__(self, lang: str, value: str):
        super().__init__(value)
        self._name = 'value'
        self._attributes = {'lang': lang}


class MultilingualString(GeneratedClassWithChildren):
    """MultilingualString -- A string of characters which may be expressed in multiple languages.
    values -- The values of the string in different languages.
    """

    def __init__(self, values: [MultilingualStringValue] = None):
        super().__init__(values)
        self._name = 'values'


class FreeOfCharge(BaseGeneratedClass):
    """Indicates whether parking is free of charge."""

    def __init__(self, content: bool):
        super().__init__(str(content).lower())
        self._name = 'freeOfCharge'



class TariffsAndPayment(GeneratedClassWithChildren):
    """TariffsAndPayment -- Details of tariffs and payment methods for parking at the parking site.
    freeOfCharge -- Indicates whether parking is free of charge.
    """

    def __init__(self, freeOfCharge: FreeOfCharge = None):
        super().__init__((freeOfCharge, ))
        self._name = 'tariffsAndPayment'


class Latitude(BaseGeneratedClass):
    """Latitude -- The latitude of a point in space."""

    def __init__(self, content: float):
        if content < -90 or content > 90:
            raise ValueError(f'Invalid number for latitude: {content}')
        super().__init__(str(content))
        self._name = 'latitude'


class Longitude(BaseGeneratedClass):
    """Longitude -- The longitude of a point in space."""

    def __init__(self, content: float):
        if content < -180 or content > 180:
            raise ValueError(f'Invalid number for longitude: {content}')
        super().__init__(str(content))
        self._name = 'longitude'


class PointCoordinates(GeneratedClassWithChildren):
    """PointCoordinates -- The coordinates of a point in space.
    latitude -- The latitude of the point.
    longitude -- The longitude of the point.
    """

    def __init__(self, latitude: Latitude, longitude: Longitude):
        super().__init__((latitude, longitude))
        self._name = 'pointCoordinates'


class PointByCoordinates(GeneratedClassWithChildren):
    """PointByCoordinates -- A point defined by coordinates.
    pointCoordinates -- The coordinates of the point."""

    def __init__(self, pointCoordinates: PointCoordinates):
        super().__init__((pointCoordinates,))
        self._name = 'pointByCoordinates'


class AssignedParkingAmongOthers(BaseGeneratedClass):
    """Assignments for parking. Other assignments are allowed as well, i.e. the parking spaces are convenient
    for this kind of assignment."""

    def __init__(self, content: str = None):
        super().__init__(content)
        self._name = 'assignedParkingAmongOthers'


class OnlyAssignedParking(BaseGeneratedClass):
    """Parking is only allowed for the assignment given in this class, i.e. other assignments are not allowed.
    By using this role, it is not allowed to use 'assignedParkingAmongOthers' and 'prohibitedParking'
    for the same type of attributes."""

    def __init__(self, content: str = None):
        super().__init__(content)
        self._name = 'onlyAssignedParking'


class ParkingLocation(GeneratedClassWithChildren):
    """ParkingLocation -- The location of a parking site or group of parking sites.
    pointByCoordinates -- A point defined by coordinates.
    """

    def __init__(self, pointByCoordinates: PointByCoordinates):
        super().__init__((pointByCoordinates,))
        self._name = 'parkingLocation'
        self._attributes = {'{http://www.w3.org/2001/XMLSchema-instance}type': 'Point'}


class ContactOrganisationName(GeneratedClassWithChildren):
    """Name of the organisation or service. Do not use this attribute in combination with role "parkingSiteAddress"."""

    def __init__(self, multilingualString: MultilingualString):
        super().__init__((multilingualString,))
        self._name = 'contactOrganisationName'


class ContactDetailsEMail(BaseGeneratedClass):
    """E-mail address of the operator."""

    def __init__(self, content: str):
        super().__init__(content)
        self._name = 'contactDetailsEMail'


class ContactDetailsTelephoneNumber(BaseGeneratedClass):
    """Telephone number of the operator."""

    def __init__(self, content: str):
        super().__init__(content)
        self._name = 'contactDetailsTelephoneNumber'


class Operator(GeneratedClassWithChildren):
    """Contact details of the operator of the parking facility.
    contactDetailsEMail -- E-mail address of the operator.
    contactDetailsTelephoneNumber -- Telephone number of the operator.
    contactOrganisationName -- Name of the organisation or service.
    Do not use this attribute in combination with role "parkingSiteAddress".
    id -- Unique identifier of the operator.
    version -- Version of the operator."""

    def __init__(self, id: str, version: str, contactOrganisationName: ContactOrganisationName,
                 contactDetailsEMail: ContactDetailsEMail, contactDetailsTelephoneNumber: ContactDetailsTelephoneNumber):
        super().__init__((contactOrganisationName, contactDetailsTelephoneNumber, contactDetailsEMail))
        self._name = 'operator'
        self._attributes = {'id': id, 'version': version,
                            '{http://www.w3.org/2001/XMLSchema-instance}type': 'ContactDetails'}


class ParkingName(GeneratedClassWithChildren):
    """ParkingName -- The name of a parking site or group of parking sites.
    name -- The name of the parking site or group of parking sites.
    """

    def __init__(self, multilingualString: MultilingualString):
        super().__init__((multilingualString,))
        self._name = 'parkingName'


class ParkingNumberOfSpaces(BaseGeneratedClass):
    """Number of parking spaces (attribute is used for a parking record as well as for a group of parking spaces)."""

    def __init__(self, parkingNumberOfSpaces: int):
        if parkingNumberOfSpaces < 0:
            raise ValueError(f'Invalid number for number of parking spaces: {parkingNumberOfSpaces}')
        super().__init__(str(parkingNumberOfSpaces))
        self._name = 'parkingNumberOfSpaces'


mapping_serviceFacilityType = {
    "Hotel": ServiceFacilityTypeEnum.Hotel,
    "Motel": ServiceFacilityTypeEnum.Motel,
    "Overnight accommodation": ServiceFacilityTypeEnum.OvernightAccommodation,
    "Shop": ServiceFacilityTypeEnum.Shop,
    "Kiosk": ServiceFacilityTypeEnum.Kiosk,
    "Food shopping": ServiceFacilityTypeEnum.FoodShopping,
    "Cafe": ServiceFacilityTypeEnum.Cafe,
    "Restaurant": ServiceFacilityTypeEnum.Restaurant,
    "Restaurant self service": ServiceFacilityTypeEnum.RestaurantSelfService,
    "Motorway restaurant": ServiceFacilityTypeEnum.MotorwayRestaurant,
    "Motorway restaurant small": ServiceFacilityTypeEnum.MotorwayRestaurantSmall,
    "Spare parts shopping": ServiceFacilityTypeEnum.SparePartsShopping,
    "Petrol station": ServiceFacilityTypeEnum.PetrolStation,
    "Vehicle maintenance": ServiceFacilityTypeEnum.VehicleMaintenance,
    "Tyre repair": ServiceFacilityTypeEnum.TyreRepair,
    "Truck repair": ServiceFacilityTypeEnum.TruckRepair,
    "Truck wash": ServiceFacilityTypeEnum.TruckWash,
    "Car wash": ServiceFacilityTypeEnum.CarWash,
    "Pharmacy": ServiceFacilityTypeEnum.Pharmacy,
    "Medical facility": ServiceFacilityTypeEnum.MedicalFacility,
    "Police": ServiceFacilityTypeEnum.Police,
    "Tourist information": ServiceFacilityTypeEnum.TouristInformation,
    "Bike sharing": ServiceFacilityTypeEnum.BikeSharing,
    "Docstop": ServiceFacilityTypeEnum.Docstop,
    "Laundry": ServiceFacilityTypeEnum.Laundry,
    "Leisure activities": ServiceFacilityTypeEnum.LeisureActivities,
    "Unknown": ServiceFacilityTypeEnum.Unknown,
    "Other": ServiceFacilityTypeEnum.Other
}

class ServiceFacilityType(BaseGeneratedClass):
    """ServiceFacilityType -- The type of service facility or equipment available at the parking site."""

    def __init__(self, content: str):
        mapped_content = mapping_serviceFacilityType[content]
        validate_serviceFacilityTypeEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'serviceFacilityType'

class ParkingEquipmentOrServiceFacility(GeneratedClassWithChildren):
    """ParkingEquipmentOrServiceFacility -- Equipment or service facility available at the parking site.
    serviceFacilityType -- The type of service facility or equipment available at the parking site.
    type -- The type of parking equipment or service facility.
    """
    def __init__(self, parkingEquipmentOrServiceFacility = None, serviceFacilityType: ServiceFacilityType=None, type_: str = None):
        super().__init__((parkingEquipmentOrServiceFacility, serviceFacilityType))
        self._name = 'parkingEquipmentOrServiceFacility'
        if type_ is not None:
            self._attributes = {'{http://www.w3.org/2001/XMLSchema-instance}type': type_}


class ParkingEquipmentOrServiceFacilityList(GeneratedIndexedListClassWithChildren):
    def __init__(self, parkingEquipmentOrServiceFacility: [ParkingEquipmentOrServiceFacility]):
        super().__init__(parkingEquipmentOrServiceFacility, index_name='equipmentOrServiceFacilityIndex')


class ParkingRecord(GeneratedClassWithChildren, abc.ABC):
    """A container for static parking information. Must be specialised as a parking site or as a group of parking sites."""

    def __init__(self, type_: str, id: str, version: str, parkingName: ParkingName=None,
                 parkingRecordVersionTime: ParkingRecordVersionTime=None, parkingLocation: ParkingLocation=None,
                 parkingNumberOfSpaces: ParkingNumberOfSpaces=None, operator: Operator=None,
                 onlyAssignedParking: OnlyAssignedParking=None,
                 assignedParkingAmongOthers: AssignedParkingAmongOthers=None, tariffsAndPayment: TariffsAndPayment=None,
                 parkingEquipmentOrServiceFacility: ParkingEquipmentOrServiceFacilityList=None,):
        super().__init__((parkingName, parkingRecordVersionTime, parkingNumberOfSpaces, operator, parkingLocation,
                          onlyAssignedParking, assignedParkingAmongOthers, tariffsAndPayment,
                          parkingEquipmentOrServiceFacility))
        self._name = 'parkingRecord'
        self._attributes = {'{http://www.w3.org/2001/XMLSchema-instance}type': type_, 'id': id, 'version': version}


class ParkingTable(GeneratedClassWithChildren):
    """A collection of parking records, which can be parking sites or groups of parking sites."""

    def __init__(self, id: str, version: str, parkingTableVersionTime: ParkingTableVersionTime,
                 parkingRecords:[ParkingRecord]=()):
        super().__init__((parkingTableVersionTime, *parkingRecords))
        self._name = 'parkingTable'
        self._attributes = {'id': id, 'version': version}


class ParkingTablePublication(GeneratedClassWithChildren):
    """ParkingTablePublication -- A publication containing a parking table.
    parkingTable -- A collection of parking records, which can be parking sites or groups of parking sites.
    """

    def __init__(self, parkingTable: ParkingTable = None):
        super().__init__((parkingTable,))
        self._name = 'parkingTablePublication'


class GenericPublicationExtension(GeneratedClassWithChildren):
    """GenericPublicationExtension -- Extension class for additional elements that are not part
    of the DATEX II standard."""

    def __init__(self, parkingTablePublication: ParkingTablePublication=None):
        super().__init__((parkingTablePublication,))
        self._name = 'genericPublicationExtension'


class PayloadPublication(GeneratedClassWithChildren):
    """PayloadPublication -- A payload publication of traffic related information or associated management information created at a specific point in time that can be exchanged via a DATEX II interface.
    lang -- The default language used throughout the payload publication.
    publicationTime -- Date/time at which the payload publication was created."""

    def __init__(self, publicationCreator=None,
                 genericPublicationName: GenericPublicationName = None,
                 genericPublicationExtension: GenericPublicationExtension = None, genericPublicationType=None,
                 lang: str = None):
        publicationCreator._name = 'publicationCreator'
        super().__init__((PublicationTime(), publicationCreator, genericPublicationName, genericPublicationExtension))
        self._name = 'payloadPublication'
        self._attributes = {'lang': lang, '{http://www.w3.org/2001/XMLSchema-instance}type': "GenericPublication"}


class D2LogicalModel:
    """D2LogicalModel -- The DATEX II logical model comprising exchange, content payload and management sub-models."""

    def __init__(self, exchange: Exchange = None, payloadPublication=None):
        self._children = (exchange, payloadPublication)
        self._namespaces = {
            '': 'http://datex2.eu/schema/2/2_0',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
        }

    def to_tree(self):
        for ns in self._namespaces:
            ET.register_namespace(ns, self._namespaces[ns])

        el_tree = ET.ElementTree(ET.Element('{http://datex2.eu/schema/2/2_0}d2LogicalModel',
                                            {'modelBaseVersion': '2'}))
        root = el_tree.getroot()
        for child in (c for c in self._children if c is not None):
            child.to_element(parent=root)

        return el_tree
