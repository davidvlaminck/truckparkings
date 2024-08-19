import abc
import datetime
from enum import Enum
import xml.etree.ElementTree as ET


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


class GeneratedClass(abc.ABC):
    @abc.abstractmethod
    def to_element(self, parent: ET.Element):
        raise NotImplementedError

    def __init__(self):
        self._name = None
        self._attributes = None


class BaseGeneratedClass(GeneratedClass):
    def __init__(self, content: str):
        super().__init__()
        self.content = content

    def to_element(self, parent: ET.Element):
        if self._attributes is None:
            el = ET.SubElement(parent, self._name)
        else:
            el = ET.SubElement(parent, self._name, attrib=self._attributes)
        el.text = self.content


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


class PublicationTime(BaseGeneratedClass):
    def __init__(self, publicationTime: str = None):
        super().__init__("")
        self._name = 'publicationTime'
        self.content = datetime.datetime.now().astimezone().isoformat()


class PayloadPublication(GeneratedClassWithChildren):
    """PayloadPublication -- A payload publication of traffic related information or associated management information created at a specific point in time that can be exchanged via a DATEX II interface.
    lang -- The default language used throughout the payload publication.
    publicationTime -- Date/time at which the payload publication was created."""

    def __init__(self, publicationTime: PublicationTime = None, publicationCreator=None, genericPublicationName=None,
                 payloadPublicationExtension=None, genericPublicationType=None, lang:str=None):
        publicationCreator._name = 'publicationCreator'
        super().__init__((PublicationTime(), publicationCreator, genericPublicationName, payloadPublicationExtension))
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
