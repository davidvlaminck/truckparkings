from enum import Enum
import xml.etree.ElementTree as ET


class CountryEnum(str, Enum):
    """CountryEnum -- List of countries.
    
    """
    AT='at' # Austria
    BE='be' # Belgium
    BG='bg' # Bulgaria
    CH='ch' # Switzerland
    CS='cs' # Serbia and Montenegro
    CY='cy' # Cyprus
    CZ='cz' # Czech Republic
    DE='de' # Germany
    DK='dk' # Denmark
    EE='ee' # Estonia
    ES='es' # Spain
    FI='fi' # Finland
    FO='fo' # Faroe Islands
    FR='fr' # France
    GB='gb' # Great Britain
    GG='gg' # Guernsey
    GI='gi' # Gibraltar
    GR='gr' # Greece
    HR='hr' # Croatia
    HU='hu' # Hungary
    IE='ie' # Ireland
    IM='im' # Isle Of Man
    IS='is' # Iceland
    IT='it' # Italy
    JE='je' # Jersey
    LI='li' # Lichtenstein
    LT='lt' # Lithuania
    LU='lu' # Luxembourg
    LV='lv' # Latvia
    MA='ma' # Morocco
    MC='mc' # Monaco
    MK='mk' # Macedonia
    MT='mt' # Malta
    NL='nl' # Netherlands
    NO='no' # Norway
    PL='pl' # Poland
    PT='pt' # Portugal
    RO='ro' # Romania
    SE='se' # Sweden
    SI='si' # Slovenia
    SK='sk' # Slovakia
    SM='sm' # San Marino
    TR='tr' # Turkey
    VA='va' # Vatican City State
    OTHER='other' # Other than as defined in this enumeration.


class NationalIdentifier:
    """NationalIdentifier -- An identifier/name unique within the specified country."""

    def __init__(self, content: str):
        self.content = content
        self._position = 1
        #self.validate_CountryEnum(self.country)

    def to_element(self, parent: ET.Element):
        el = ET.SubElement(parent, 'nationalIdentifier')
        el.text = self.content


class Country:
    """Country -- A country."""

    def __init__(self, content: CountryEnum):
        self.content = content
        self._position = 0
        #self.validate_CountryEnum(self.country)

    def to_element(self, parent: ET.Element):
        el = ET.SubElement(parent, 'country')
        el.text = self.content


class InternationalIdentifier:
    """InternationalIdentifier -- An identifier/name whose range is specific to the particular country.
    country -- ISO 3166-1 two character country code.
    nationalIdentifier -- Identifier or name unique within the specified country.

    """

    def __init__(self, country: Country = None, nationalIdentifier: NationalIdentifier = None, internationalIdentifierExtension=None):
        self.country = country
        self.nationalIdentifier = nationalIdentifier
        self.internationalIdentifierExtension = internationalIdentifierExtension
        self._children = {self.country, self.nationalIdentifier, self.internationalIdentifierExtension}

    def to_element(self, parent: ET.Element):
        el = ET.SubElement(parent, 'supplierIdentification')

        for child in sorted([c for c in self._children if c is not None], key=lambda x:x._position):
            child.to_element(parent=el)

class Exchange:
    """Exchange -- Details associated with the management of the exchange between the supplier and the client."""
    def __init__(self, supplierIdentification: InternationalIdentifier = None, exchangeExtension=None):
        self.supplierIdentification = supplierIdentification
        self.exchangeExtension = exchangeExtension
        self._children = {self.supplierIdentification, self.exchangeExtension}

    def to_element(self, parent: ET.Element):
        el = ET.SubElement(parent, 'exchange')

        for child in self._children:
            if child is not None:
                child.to_element(parent=el)


class D2LogicalModel:
    """D2LogicalModel -- The DATEX II logical model comprising exchange, content payload and management sub-models."""

    def __init__(self, exchange: Exchange = None, payloadPublication=None):
        self.exchange = exchange
        self.payloadPublication = payloadPublication
        self._children = {self.exchange, self.payloadPublication}

    def to_tree(self):
        ET.register_namespace('', 'http://datex2.eu/schema/2/2_0')
        ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        el_tree = ET.ElementTree(ET.Element('{http://datex2.eu/schema/2/2_0}d2LogicalModel',
                                       {'modelBaseVersion': '2'}))
        root = el_tree.getroot()
        for child in self._children:
            if child is not None:
                child.to_element(parent=root)

        return el_tree
