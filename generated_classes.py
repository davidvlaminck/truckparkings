import abc
import datetime
from enum import Enum
import xml.etree.ElementTree as ET


class InterUrbanParkingSiteLocationEnum(str, Enum):
    """Location of the truck or motorway related parking."""
    Motorway = 'motorway'
    NearbyMotorway = 'nearbyMotorway'
    LayBy = 'layBy'
    OnStreet = 'onStreet'
    Other = 'other'


class ParkingSecurityEnum(str, Enum):
    """Specifies security measures related to the parking site or particular spaces."""
    SocialControl = 'socialControl'
    SecurityStaff = 'securityStaff'
    ExternalSecurity = 'externalSecurity'
    CCTV = 'cctv'
    Dog = 'dog'
    Guard24Hours = 'guard24hours'
    Lighting = 'lighting'
    FloodLight = 'floodLight'
    Fences = 'fences'
    AreaSeperatedFromSurroundings = 'areaSeperatedFromSurroundings'
    None_ = 'none'
    Unknown = 'unknown'
    Other = 'other'


class ServiceLevelEnum(str, Enum):
    """Service level defined by the LABEL project http://truckparkinglabel.eu."""
    None_ = 'none'
    ServiceLevel1 = 'serviceLevel1'
    ServiceLevel2 = 'serviceLevel2'
    ServiceLevel3 = 'serviceLevel3'
    ServiceLevel4 = 'serviceLevel4'
    ServiceLevel5 = 'serviceLevel5'
    Unknown = 'unknown'


class LabelSecurityLevelEnum(str, Enum):
    """Security level defined by the LABEL project http://truckparkinglabel.eu."""
    None_ = 'none'
    SecurityLevel1 = 'securityLevel1'
    SecurityLevel2 = 'securityLevel2'
    SecurityLevel3 = 'securityLevel3'
    SecurityLevel4 = 'securityLevel4'
    SecurityLevel5 = 'securityLevel5'
    Unknown = 'unknown'


class AccessCategoryEnum(str, Enum):
    """Specifies the category of the access."""
    VehicleEntranceAndExit = 'vehicleEntranceAndExit'
    VehicleEntrance = 'vehicleEntrance'

class LoadTypeEnum(str, Enum):
    """LoadTypeEnum -- List of types of load that may be carried by a vehicle."""
    Animals = 'animals'
    Asbestos = 'asbestos'
    Beverages = 'beverages'
    BuildingMaterials = 'buildingMaterials'
    Chemicals = 'chemicals'
    CombustibleMaterials = 'combustibleMaterials'
    CorrosiveMaterials = 'corrosiveMaterials'
    Debris = 'debris'
    Empty = 'empty'
    ExplosiveMaterials = 'explosiveMaterials'
    ExtraHighLoad = 'extraHighLoad'
    ExtraLongLoad = 'extraLongLoad'
    ExtraWideLoad = 'extraWideLoad'
    Fuel = 'fuel'
    Glass = 'glass'
    Goods = 'goods'
    HazardousMaterials = 'hazardousMaterials'
    Liquid = 'liquid'
    Livestock = 'livestock'
    Materials = 'materials'
    MaterialsDangerousForPeople = 'materialsDangerousForPeople'
    MaterialsDangerousForTheEnvironment = 'materialsDangerousForTheEnvironment'
    MaterialsDangerousForWater = 'materialsDangerousForWater'
    Oil = 'oil'
    Ordinary = 'ordinary'
    PerishableProducts = 'perishableProducts'
    Petrol = 'petrol'
    PharmaceuticalMaterials = 'pharmaceuticalMaterials'
    RadioactiveMaterials = 'radioactiveMaterials'
    Refuse = 'refuse'
    ToxicMaterials = 'toxicMaterials'
    Vehicles = 'vehicles'
    Other = 'other'


class VehicleTypeEnum(str, Enum):
    AgriculturalVehicle = 'agriculturalVehicle'
    AnyVehicle = 'anyVehicle'
    ArticulatedVehicle = 'articulatedVehicle'
    Bicycle = 'bicycle'
    Bus = 'bus'
    Car = 'car'
    Caravan = 'caravan'
    CarOrLightVehicle = 'carOrLightVehicle'
    CarWithCaravan = 'carWithCaravan'
    CarWithTrailer = 'carWithTrailer'
    ConstructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    FourWheelDrive = 'fourWheelDrive'
    HighSidedVehicle = 'highSidedVehicle'
    Lorry = 'lorry'
    Moped = 'moped'
    Motorcycle = 'motorcycle'
    MotorcycleWithSideCar = 'motorcycleWithSideCar'
    Motorscooter = 'motorscooter'
    Tanker = 'tanker'
    ThreeWheeledVehicle = 'threeWheeledVehicle'
    Trailer = 'trailer'
    Tram = 'tram'
    TwoWheeledVehicle = 'twoWheeledVehicle'
    Van = 'van'
    VehicleWithCatalyticConverter = 'vehicleWithCatalyticConverter'
    VehicleWithoutCatalyticConverter = 'vehicleWithoutCatalyticConverter'
    VehicleWithCaravan = 'vehicleWithCaravan'
    VehicleWithTrailer = 'vehicleWithTrailer'
    WithEvenNumberedRegistrationPlates = 'withEvenNumberedRegistrationPlates'
    WithOddNumberedRegistrationPlates = 'withOddNumberedRegistrationPlates'
    Other = 'other'


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


def validate_interUrbanParkingSiteLocationEnum(interUrbanParkingSiteLocation) -> bool:
    if interUrbanParkingSiteLocation not in InterUrbanParkingSiteLocationEnum:
        raise ValueError(f'Invalid interUrbanParkingSiteLocation: {interUrbanParkingSiteLocation}')
    return True


def validate_parkingSecurityEnum(parkingSecurity) -> bool:
    if parkingSecurity not in ParkingSecurityEnum:
        raise ValueError(f'Invalid parkingSecurity: {parkingSecurity}')
    return True


def validate_ServiceLevelEnum(serviceLevel) -> bool:
    if serviceLevel not in ServiceLevelEnum:
        raise ValueError(f'Invalid serviceLevel: {serviceLevel}')
    return True


def validate_accessCategoryEnum(accessCategory) -> bool:
    if accessCategory not in AccessCategoryEnum:
        raise ValueError(f'Invalid accessCategory: {accessCategory}')
    return True


def validate_labelSecurityLevelEnum(labelSecurityLevel) -> bool:
    if labelSecurityLevel not in LabelSecurityLevelEnum:
        raise ValueError(f'Invalid labelSecurityLevel: {labelSecurityLevel}')
    return True


def validate_countryEnum(country) -> bool:
    if country not in CountryEnum:
        raise ValueError(f'Invalid country: {country}')
    return True


def validate_vehicleTypeEnum(vehicleType) -> bool:
    if vehicleType not in VehicleTypeEnum:
        raise ValueError(f'Invalid vehicleType: {vehicleType}')
    return True


def validate_serviceFacilityTypeEnum(serviceFacilityType) -> bool:
    if serviceFacilityType not in ServiceFacilityTypeEnum:
        raise ValueError(f'Invalid ServiceFacilityType: {serviceFacilityType}')
    return True


def validate_loadTypeEnum(loadType) -> bool:
    if loadType not in LoadTypeEnum:
        raise ValueError(f'Invalid loadType: {loadType}')
    return True


mapping_interUrbanParkingSiteLocation = {
    "motorway": InterUrbanParkingSiteLocationEnum.Motorway,
    "nearbyMotorway": InterUrbanParkingSiteLocationEnum.NearbyMotorway,
    "layBy": InterUrbanParkingSiteLocationEnum.LayBy,
    "onStreet": InterUrbanParkingSiteLocationEnum.OnStreet,
    "other": InterUrbanParkingSiteLocationEnum.Other
}


mapping_parkingSecurity = {
    "socialControl": ParkingSecurityEnum.SocialControl,
    "securityStaff": ParkingSecurityEnum.SecurityStaff,
    "externalSecurity": ParkingSecurityEnum.ExternalSecurity,
    "cctv": ParkingSecurityEnum.CCTV,
    "dog": ParkingSecurityEnum.Dog,
    "guard24hours": ParkingSecurityEnum.Guard24Hours,
    "lighting": ParkingSecurityEnum.Lighting,
    "floodLight": ParkingSecurityEnum.FloodLight,
    "fences": ParkingSecurityEnum.Fences,
    "areaSeperatedFromSurroundings": ParkingSecurityEnum.AreaSeperatedFromSurroundings,
    "none": ParkingSecurityEnum.None_,
    "unknown": ParkingSecurityEnum.Unknown,
    "other": ParkingSecurityEnum.Other
}

mapping_labelSecurityLevel = {
    "none": LabelSecurityLevelEnum.None_,
    "securityLevel1": LabelSecurityLevelEnum.SecurityLevel1,
    "securityLevel2": LabelSecurityLevelEnum.SecurityLevel2,
    "securityLevel3": LabelSecurityLevelEnum.SecurityLevel3,
    "securityLevel4": LabelSecurityLevelEnum.SecurityLevel4,
    "securityLevel5": LabelSecurityLevelEnum.SecurityLevel5,
    "unknown": LabelSecurityLevelEnum.Unknown
}

mapping_LabelServiceLevel = {
    "none": ServiceLevelEnum.None_,
    "serviceLevel1": ServiceLevelEnum.ServiceLevel1,
    "serviceLevel2": ServiceLevelEnum.ServiceLevel2,
    "serviceLevel3": ServiceLevelEnum.ServiceLevel3,
    "serviceLevel4": ServiceLevelEnum.ServiceLevel4,
    "serviceLevel5": ServiceLevelEnum.ServiceLevel5,
    "unknown": ServiceLevelEnum.Unknown
}


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

mapping_vehicleType = {
    "Agricultural vehicle": VehicleTypeEnum.AgriculturalVehicle,
    "Any vehicle": VehicleTypeEnum.AnyVehicle,
    "Articulated vehicle": VehicleTypeEnum.ArticulatedVehicle,
    "Bicycle": VehicleTypeEnum.Bicycle,
    "Bus": VehicleTypeEnum.Bus,
    "Car": VehicleTypeEnum.Car,
    "Caravan": VehicleTypeEnum.Caravan,
    "Car or light vehicle": VehicleTypeEnum.CarOrLightVehicle,
    "Car with caravan": VehicleTypeEnum.CarWithCaravan,
    "Car with trailer": VehicleTypeEnum.CarWithTrailer,
    "Construction or maintenance vehicle": VehicleTypeEnum.ConstructionOrMaintenanceVehicle,
    "Four wheel drive": VehicleTypeEnum.FourWheelDrive,
    "High sided vehicle": VehicleTypeEnum.HighSidedVehicle,
    "Lorry": VehicleTypeEnum.Lorry,
    "Moped": VehicleTypeEnum.Moped,
    "Motorcycle": VehicleTypeEnum.Motorcycle,
    "Motorcycle with side car": VehicleTypeEnum.MotorcycleWithSideCar,
    "Motorscooter": VehicleTypeEnum.Motorscooter,
    "Tanker": VehicleTypeEnum.Tanker,
    "Three wheeled vehicle": VehicleTypeEnum.ThreeWheeledVehicle,
    "Trailer": VehicleTypeEnum.Trailer,
    "Tram": VehicleTypeEnum.Tram,
    "Two wheeled vehicle": VehicleTypeEnum.TwoWheeledVehicle,
    "Van": VehicleTypeEnum.Van,
    "Vehicle with catalytic converter": VehicleTypeEnum.VehicleWithCatalyticConverter,
    "Vehicle without catalytic converter": VehicleTypeEnum.VehicleWithoutCatalyticConverter,
    "Vehicle with caravan": VehicleTypeEnum.VehicleWithCaravan,
    "Vehicle with trailer": VehicleTypeEnum.VehicleWithTrailer,
    "With even numbered registration plates": VehicleTypeEnum.WithEvenNumberedRegistrationPlates,
    "With odd numbered registration plates": VehicleTypeEnum.WithOddNumberedRegistrationPlates,
    "Other": VehicleTypeEnum.Other
}

mapping_loadType = {
    "Animals": LoadTypeEnum.Animals,
    "Asbestos": LoadTypeEnum.Asbestos,
    "Beverages": LoadTypeEnum.Beverages,
    "Building materials": LoadTypeEnum.BuildingMaterials,
    "Chemicals": LoadTypeEnum.Chemicals,
    "Combustible materials": LoadTypeEnum.CombustibleMaterials,
    "Corrosive materials": LoadTypeEnum.CorrosiveMaterials,
    "Debris": LoadTypeEnum.Debris,
    "Empty": LoadTypeEnum.Empty,
    "Explosive materials": LoadTypeEnum.ExplosiveMaterials,
    "Extra high load": LoadTypeEnum.ExtraHighLoad,
    "Extra long load": LoadTypeEnum.ExtraLongLoad,
    "Extra wide load": LoadTypeEnum.ExtraWideLoad,
    "Fuel": LoadTypeEnum.Fuel,
    "Glass": LoadTypeEnum.Glass,
    "Goods": LoadTypeEnum.Goods,
    "Hazardous materials": LoadTypeEnum.HazardousMaterials,
    "Liquid": LoadTypeEnum.Liquid,
    "Livestock": LoadTypeEnum.Livestock,
    "Materials": LoadTypeEnum.Materials,
    "Materials dangerous for people": LoadTypeEnum.MaterialsDangerousForPeople,
    "Materials dangerous for the environment": LoadTypeEnum.MaterialsDangerousForTheEnvironment,
    "Materials dangerous for water": LoadTypeEnum.MaterialsDangerousForWater,
    "Oil": LoadTypeEnum.Oil,
    "Ordinary": LoadTypeEnum.Ordinary,
    "Perishable products": LoadTypeEnum.PerishableProducts,
    "Petrol": LoadTypeEnum.Petrol,
    "Pharmaceutical materials": LoadTypeEnum.PharmaceuticalMaterials,
    "Radioactive materials": LoadTypeEnum.RadioactiveMaterials,
    "Refuse": LoadTypeEnum.Refuse,
    "Toxic materials": LoadTypeEnum.ToxicMaterials,
    "Vehicles": LoadTypeEnum.Vehicles,
    "Other": LoadTypeEnum.Other
}

mapping_accessCategory = {
    "vehicle entrance and exit": AccessCategoryEnum.VehicleEntranceAndExit,
    "vehicle entrance": AccessCategoryEnum.VehicleEntrance
}


class GeneratedClass(abc.ABC):
    @abc.abstractmethod
    def to_element(self, parent: ET.Element):
        raise NotImplementedError

    def __init__(self):
        self._name = None
        self._attributes = None

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

    def __repr__(self):
        return self.__str__()


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

        if self._children is None:
            return

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
        super().__init__(children=(pointCoordinates,))
        self._name = 'pointByCoordinates'


class VehicleType(BaseGeneratedClass):
    """VehicleType -- The type of vehicle."""

    def __init__(self, content: str):
        mapped_content = mapping_vehicleType[content]
        validate_vehicleTypeEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'vehicleType'


class LoadType(BaseGeneratedClass):
    """LoadType -- The type of load."""

    def __init__(self, content: str):
        if content is None:
            super().__init__(None)
            return
        mapped_content = mapping_loadType[content]
        validate_loadTypeEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'loadType'


class VehicleCharacteristics(GeneratedClassWithChildren):
    """VehicleCharacteristics -- Characteristics of a vehicle.
    vehicleType -- The type of vehicle.
    loadType -- The type of load carried by the vehicle.
    """

    def __init__(self, vehicleType: VehicleType = None, loadType: LoadType = None):
        super().__init__(children=(vehicleType, loadType))
        self._name = 'vehicleCharacteristics'


class AssignedParkingAmongOthers(GeneratedClassWithChildren):
    """Assignments for parking. Other assignments are allowed as well, i.e. the parking spaces are convenient
    for this kind of assignment."""

    def __init__(self, vehicleCharacteristics: VehicleCharacteristics = None):
        super().__init__(children=(vehicleCharacteristics,))
        self._name = 'assignedParkingAmongOthers'


class OnlyAssignedParking(BaseGeneratedClass):
    """Parking is only allowed for the assignment given in this class, i.e. other assignments are not allowed.
    By using this role, it is not allowed to use 'assignedParkingAmongOthers' and 'prohibitedParking'
    for the same type of attributes."""

    def __init__(self, content: str = None):
        super().__init__(content)
        self._name = 'onlyAssignedParking'


class ContactDetails(BaseGeneratedClass):
    """ContactDetails -- Details of the contact person or organisation.
    """

    def __init__(self):
        super().__init__("")
        self._name = 'contactDetails'
        raise NotImplementedError()



class ParkingsSiteAddress(GeneratedClassWithChildren):
    """ParkingsSiteAddress -- The address of a parking site or group of parking sites.
    country -- The country of the parking site.
    nationalIdentifier -- Identifier or name unique within the specified country.
    """

    def __init__(self, id: str, version: str, contactDetails: ContactDetails=None):
        super().__init__((contactDetails,))
        self._name = 'parkingSiteAddress'
        self._attributes = {'id': id, 'version': version,
                            '{http://www.w3.org/2001/XMLSchema-instance}type': 'ContactDetails'}


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


class ParkingTypeOfGroup(BaseGeneratedClass):
    """ParkingTypeOfGroup -- The type of group of parking spaces."""

    def __init__(self, content: str):
        super().__init__(content)
        self._name = 'parkingTypeOfGroup'


class ParkingSpaceBasics(GeneratedClassWithChildren):
    """ParkingSpaceBasics -- Basic information about a parking space.
    parkingTypeOfGroup -- The type of group of parking spaces.
    parkingNumberOfSpaces -- Number of parking spaces in the group.
    assignedParkingAmongOthers -- Assignments for parking. Other assignments are allowed as well, i.e. the parking spaces are convenient for this kind of assignment.
    """

    def __init__(self, type_: str, assignedParkingAmongOthers: AssignedParkingAmongOthers,
                 parkingNumberOfSpaces: ParkingNumberOfSpaces=None, parkingTypeOfGroup: ParkingTypeOfGroup = None):
        super().__init__((assignedParkingAmongOthers, parkingNumberOfSpaces, parkingTypeOfGroup))
        self._name = 'parkingSpaceBasics'
        self._attributes = {'{http://www.w3.org/2001/XMLSchema-instance}type': type_}


class GroupOfParkingSpaces(GeneratedClassWithChildren):
    """GroupOfParkingSpaces -- A group of parking spaces with the same characteristics.
    parkingSpaceBasics -- Basic information about the parking spaces in the group.
    """

    def __init__(self, parkingSpaceBasics: ParkingSpaceBasics):
        super().__init__((parkingSpaceBasics,))
        self._name = 'groupOfParkingSpaces'


class GroupOfParkingSpacesList(GeneratedIndexedListClassWithChildren):
    def __init__(self, groupOfParkingSpaces: [GroupOfParkingSpaces]):
        super().__init__(groupOfParkingSpaces, index_name='groupIndex')


class Location(GeneratedClassWithChildren):
    """Location -- The location of the parking site or group of parking sites.
    pointByCoordinates -- A point defined by coordinates.
    """

    def __init__(self, pointByCoordinates: PointByCoordinates):
        super().__init__((pointByCoordinates,))
        self._name = 'location'
        self._attributes = {'{http://www.w3.org/2001/XMLSchema-instance}type': 'Point'}


class AccessCategory(BaseGeneratedClass):
    """AccessCategory -- The category of the access."""

    def __init__(self, content: str):
        mapped_content = mapping_accessCategory[content]
        validate_accessCategoryEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'accessCategory'

class RoadIdentifier(GeneratedClassWithChildren):
    """RoadIdentifier -- An identifier for a road."""

    def __init__(self, multilingualString: MultilingualString):
        super().__init__((multilingualString,))
        self._name = 'roadIdentifier'


class NameOfRoad(GeneratedClassWithChildren):
    """NameOfRoad -- The name of a road."""

    def __init__(self, multilingualString: MultilingualString):
        super().__init__((multilingualString,))
        self._name = 'nameOfRoad'


class RoadDestination(GeneratedClassWithChildren):
    """RoadDestination -- The destination of a road."""

    def __init__(self, multilingualString: MultilingualString):
        super().__init__((multilingualString,))
        self._name = 'roadDestination'


class PrimaryRoad(GeneratedClassWithChildren):
    """PrimaryRoad -- The primary road on which the parking site is located."""

    def __init__(self, nameOfRoad: NameOfRoad, roadIdentifier: RoadIdentifier, roadDestination: RoadDestination):
        super().__init__((nameOfRoad, roadIdentifier, roadDestination))
        self._name = 'primaryRoad'


class ParkingSecurity(BaseGeneratedClass):
    """ParkingSecurity -- The security level of the parking site."""

    def __init__(self, content: str):
        if content is None or content == []:
            content = 'unknown'
        mapped_content = mapping_parkingSecurity[content]
        validate_parkingSecurityEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'parkingSecurity'


class LabelServiceLevel(BaseGeneratedClass):
    """LabelServiceLevel -- The service level of the parking site."""

    def __init__(self, content: str):
        if content is None:
            content = 'unknown'
        mapped_content = mapping_LabelServiceLevel[content]
        validate_ServiceLevelEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'labelServiceLevel'


class LabelSecurityLevel(BaseGeneratedClass):
    """LabelSecurityLevel -- The security level of the parking site."""

    def __init__(self, content: str):
        if content is None:
            content = 'unknown'
        mapped_content = mapping_labelSecurityLevel[content]
        validate_labelSecurityLevelEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'labelSecurityLevel'


class ParkingStandardsAndSecurity(GeneratedClassWithChildren):
    """ParkingStandardsAndSecurity -- Standards and security at the parking site.
    """

    def __init__(self, labelSecurityLevel: LabelSecurityLevel = None, labelServiceLevel: LabelServiceLevel = None,
                 parkingSecurity: ParkingSecurity = None):
        super().__init__((labelSecurityLevel, labelServiceLevel, parkingSecurity))
        self._name = 'parkingStandardsAndSecurity'


class ParkingAccess(GeneratedClassWithChildren):
    """ParkingAccess -- Access to the parking site or group of parking sites.
    accessType -- The type of access to the parking site or group of parking sites.
    """

    def __init__(self, id: str, accessCategory: AccessCategory, primaryRoad: PrimaryRoad = None,
                 location: Location = None):
        super().__init__((accessCategory, primaryRoad, location))
        self._name = 'parkingAccess'
        self._attributes = {'id': id}


class InterUrbanParkingSiteLocation(BaseGeneratedClass):
    """InterUrbanParkingSiteLocation -- The location of an inter-urban parking site."""

    def __init__(self, content: str):
        if content is None:
            content = 'other'
        mapped_content = mapping_interUrbanParkingSiteLocation[content]
        validate_interUrbanParkingSiteLocationEnum(mapped_content)
        super().__init__(mapped_content.value)
        self._name = 'interUrbanParkingSiteLocation'


class ParkingRecord(GeneratedClassWithChildren, abc.ABC):
    """A container for static parking information. Must be specialised as a parking site or as a group of parking sites."""

    def __init__(self, type_: str, id: str, version: str, parkingName: ParkingName=None,
                 parkingRecordVersionTime: ParkingRecordVersionTime=None, parkingLocation: ParkingLocation=None,
                 parkingNumberOfSpaces: ParkingNumberOfSpaces=None, operator: Operator=None,
                 onlyAssignedParking: OnlyAssignedParking=None,
                 assignedParkingAmongOthers: AssignedParkingAmongOthers=None, tariffsAndPayment: TariffsAndPayment=None,
                 parkingEquipmentOrServiceFacility: ParkingEquipmentOrServiceFacilityList=None,
                 groupOfParkingSpaces: GroupOfParkingSpacesList=None, parkingSiteAddress: ParkingsSiteAddress=None,
                 parkingAccess: ParkingAccess=None, parkingStandardsAndSecurity: ParkingStandardsAndSecurity=None,
                 interUrbanParkingSiteLocation: InterUrbanParkingSiteLocation=None):
        super().__init__((parkingName, parkingRecordVersionTime, parkingNumberOfSpaces, operator, parkingLocation,
                          onlyAssignedParking, assignedParkingAmongOthers, tariffsAndPayment,
                          parkingEquipmentOrServiceFacility, groupOfParkingSpaces, parkingSiteAddress, parkingAccess,
                          parkingStandardsAndSecurity, interUrbanParkingSiteLocation))
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
