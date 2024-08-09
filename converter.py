import xml.etree.ElementTree as ET
from pathlib import Path

from generated_classes import D2LogicalModel, Exchange, InternationalIdentifier, CountryEnum


def convert_json_to_xml(json_path: Path, xml_path: Path):
    d2_root = D2LogicalModel()
    d2_root.exchange = Exchange()
    d2_root.exchange.supplierIdentification = InternationalIdentifier(country=CountryEnum.BE,
                                                                      nationalIdentifier="Vlaamse Overheid")

    XSI = 'http://www.w3.org/2001/XMLSchema-instance'

    # ET.register_namespace('xsd', 'http://www.w3.org/2001/XMLSchema')

    tree = ET.ElementTree(
        ET.Element('D2LogicalModel', {'xmlns': 'http://datex2.eu/schema/2/2_3', 'modelBaseVersion': '2'}))
    root = tree.getroot()

    exchange = ET.SubElement(root, 'exchange')
    supplierIdentification = ET.SubElement(exchange, 'supplierIdentification')
    country = ET.SubElement(supplierIdentification, 'country')
    country.text = CountryEnum.BE
    nationalIdentifier = ET.SubElement(supplierIdentification, 'nationalIdentifier')
    nationalIdentifier.text = 'Vlaamse Overheid'
    payloadPublication = ET.SubElement(root, 'payloadPublication', {'lang': 'DUTCH'})

    payloadPublication.set(ET.QName(XSI, 'type'), 'GenericPublication')

    tree.write(xml_path, encoding='utf-8', xml_declaration=True)
