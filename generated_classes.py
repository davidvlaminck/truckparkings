from enum import Enum


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

class InternationalIdentifier:
    """InternationalIdentifier -- An identifier/name whose range is specific to the particular country.
    country -- ISO 3166-1 two character country code.
    nationalIdentifier -- Identifier or name unique within the specified country.

    """

    def __init__(self, country: CountryEnum = None, nationalIdentifier: str = None, internationalIdentifierExtension=None):
        self.country = country
        #self.validate_CountryEnum(self.country)
        self.nationalIdentifier = nationalIdentifier
        self.internationalIdentifierExtension = internationalIdentifierExtension


class Exchange:
    """Exchange -- Details associated with the management of the exchange between the supplier and the client.

    """

    def __init__(self, supplierIdentification: InternationalIdentifier = None, exchangeExtension=None):
        self.supplierIdentification = supplierIdentification
        self.exchangeExtension = exchangeExtension


class D2LogicalModel:
    """D2LogicalModel -- The DATEX II logical model comprising exchange, content payload and management sub-models.

    """

    def __init__(self, exchange: Exchange = None, payloadPublication=None):
        self.exchange = exchange
        self.payloadPublication = payloadPublication
