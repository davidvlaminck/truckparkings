import json
import xml.etree.ElementTree as ET
from pathlib import Path

from generated_classes import D2LogicalModel, Exchange, InternationalIdentifier, CountryEnum, Country, \
    NationalIdentifier, PayloadPublication, PublicationCreator, GenericPublicationName, GenericPublicationExtension, \
    ParkingTable, ParkingTablePublication, ParkingTableVersionTime, ParkingRecord, ParkingName, MultilingualString, \
    MultilingualStringValue, ParkingRecordVersionTime, ParkingNumberOfSpaces, ContactOrganisationName, Operator, \
    ContactDetailsEMail, ContactDetailsTelephoneNumber, Longitude, Latitude, PointCoordinates, PointByCoordinates, \
    ParkingLocation, OnlyAssignedParking, AssignedParkingAmongOthers, TariffsAndPayment, FreeOfCharge, \
    ParkingEquipmentOrServiceFacilityList, ParkingEquipmentOrServiceFacility, ServiceFacilityType, GroupOfParkingSpaces, \
    ParkingSpaceBasics, GroupOfParkingSpacesList, ParkingTypeOfGroup, VehicleCharacteristics, VehicleType, \
    ParkingsSiteAddress, LoadType, ParkingAccess, AccessCategory, PrimaryRoad, NameOfRoad, RoadIdentifier, \
    RoadDestination, Location, ParkingStandardsAndSecurity, LabelSecurityLevel, LabelServiceLevel, ParkingSecurity


def convert_json_to_xml(json_path: Path, xml_path: Path):
    dict = read_json(json_path)
    tree = convert_dict_to_el_tree(dict)
    tree.write(xml_path, encoding='utf-8', xml_declaration=True)


def read_json(json_path: Path) -> dict:
    with open(json_path, 'r') as f:
        return json.load(f)


def create_parkingrecord_from_dict(p: dict, version: str) -> ParkingRecord:
    groupOfParkingSpaces = []
    for group in p['groupOfParkingSpaces']:
        groupOfParkingSpaces.append(
            GroupOfParkingSpaces(
                parkingSpaceBasics=ParkingSpaceBasics(
                    type_='GroupOfParkingSpaces',
                    parkingTypeOfGroup=ParkingTypeOfGroup(group['parkingSpaceBasics']['parkingTypeOfGroup']),
                    parkingNumberOfSpaces=ParkingNumberOfSpaces(group['parkingSpaceBasics']['parkingNumberOfSpaces']),
                    assignedParkingAmongOthers=AssignedParkingAmongOthers(
                        vehicleCharacteristics=VehicleCharacteristics(vehicleType=VehicleType(
                            group['parkingSpaceBasics']['assignedParkingAmongOthers']['vehicleCharacteristics'][
                                'vehicleType']),
                            loadType=LoadType(group['parkingSpaceBasics']['assignedParkingAmongOthers'][
                                              'vehicleCharacteristics'].get('loadType', None)))))))


    parkingEquipmentOrServiceFacilities = []
    for service_facility in p['parkingEquipmentOrServiceFacility']:
        parkingEquipmentOrServiceFacilities.append(
            ParkingEquipmentOrServiceFacility(ParkingEquipmentOrServiceFacility(
                serviceFacilityType=ServiceFacilityType(service_facility['serviceFacilityType']),
                type_=service_facility['type'])))

    parkingSiteAddress = ParkingsSiteAddress(id='', version=version)
    if p['parkingSiteAddress'] is not None:
        parkingSiteAddress = ParkingsSiteAddress(id=p['parkingSiteAddress']['id'], version=version)

    record = ParkingRecord(
        type_='InterUrbanParkingSite', id='c00134eb-dbd1-4b04-9b5d-a0834cc9193e',
        version=version,
        parkingName=ParkingName(
            multilingualString=MultilingualString(
                values=[MultilingualStringValue(value='E40 Heverlee Luik - Brussel', lang='DUTCH')])),
        parkingRecordVersionTime=ParkingRecordVersionTime(),
        parkingNumberOfSpaces=ParkingNumberOfSpaces(p['parkingNumberOfSpaces']),
        operator=Operator(
            id=p['operator']['id'], version=version,
            contactOrganisationName=ContactOrganisationName(multilingualString=MultilingualString(
                values=[MultilingualStringValue(value=str(p['operator']['contactOrganisationName']), lang='DUTCH')])),
            contactDetailsEMail=ContactDetailsEMail(p['operator']['contactDetailsEMail']),
            contactDetailsTelephoneNumber=ContactDetailsTelephoneNumber(p['operator']['contactDetailsTelephoneNumber'])
        ),
        parkingLocation=ParkingLocation(pointByCoordinates=PointByCoordinates(pointCoordinates=PointCoordinates(
            latitude=Latitude(p['parkingLocation']['pointByCoordinates']['pointCoordinates']['latitude']),
            longitude=Longitude(p['parkingLocation']['pointByCoordinates']['pointCoordinates']['longitude'])))),
        onlyAssignedParking=OnlyAssignedParking(),
        assignedParkingAmongOthers=AssignedParkingAmongOthers(),
        tariffsAndPayment=TariffsAndPayment(freeOfCharge=FreeOfCharge('freeOfCharge' in p['tariffsAndPayment'])),
        parkingEquipmentOrServiceFacility=ParkingEquipmentOrServiceFacilityList(parkingEquipmentOrServiceFacilities,),
        groupOfParkingSpaces=GroupOfParkingSpacesList(groupOfParkingSpaces),
        parkingSiteAddress=parkingSiteAddress,
        parkingAccess=ParkingAccess(
            id=p['parkingAccess']['id'], accessCategory=AccessCategory(p['parkingAccess']['accessCategory']),
            primaryRoad=PrimaryRoad(
                nameOfRoad=NameOfRoad(multilingualString=MultilingualString(values=[
                    MultilingualStringValue(value=p['parkingAccess']['PrimaryRoad'][0]['nameOfRoad'],
                                            lang='DUTCH')])),
                roadIdentifier=RoadIdentifier(multilingualString=MultilingualString(values=[
                    MultilingualStringValue(value=p['parkingAccess']['PrimaryRoad'][0]['roadIdentifier'],
                                            lang='DUTCH')])),
                roadDestination=RoadDestination(multilingualString=MultilingualString(values=[
                    MultilingualStringValue(value=p['parkingAccess']['PrimaryRoad'][0]['roadDestination'],
                                            lang='DUTCH')]))),
            location=Location(pointByCoordinates=PointByCoordinates(pointCoordinates=PointCoordinates(
                latitude=Latitude(p['parkingAccess']['location'][0]['pointByCoordinates']['pointCoordinates']['latitude']),
                longitude=Longitude(p['parkingAccess']['location'][0]['pointByCoordinates']['pointCoordinates']['longitude']))))
        ),
        parkingStandardsAndSecurity=ParkingStandardsAndSecurity(
            labelSecurityLevel=LabelSecurityLevel(p['parkingStandardsAndSecurity']['labelSecurityLevel']),
            labelServiceLevel=LabelServiceLevel(p['parkingStandardsAndSecurity']['labelServiceLevel']),
            parkingSecurity=ParkingSecurity(p['parkingStandardsAndSecurity']['parkingSecurity'])),
    )

    return record


def convert_dict_to_el_tree(data_dict: dict, parking_table_id: str = '', version: str = '') -> ET.ElementTree:
    parking_table = ParkingTable(id=parking_table_id, version=version,
                                 parkingTableVersionTime=ParkingTableVersionTime(),
                                 parkingRecords=[create_parkingrecord_from_dict(p=p, version=version)
                                                 for p in data_dict['parkings']])

    d2_root = D2LogicalModel(
        exchange=Exchange(
            supplierIdentification=InternationalIdentifier(
                country=Country('be'), nationalIdentifier=NationalIdentifier("Vlaamse Overheid"))),
        payloadPublication=PayloadPublication(
            genericPublicationExtension=GenericPublicationExtension(
                parkingTablePublication=ParkingTablePublication(
                    parkingTable=parking_table)),
            genericPublicationName=GenericPublicationName('ParkingTablePublication'),
            publicationCreator=PublicationCreator(InternationalIdentifier(
                country=Country('be'), nationalIdentifier=NationalIdentifier("Vlaamse Overheid"))),
            lang='DUTCH', genericPublicationType='GenericPublication'))
    return d2_root.to_tree()

    XSI = 'http://www.w3.org/2001/XMLSchema-instance'

    # payloadPublication = ET.SubElement(root, 'payloadPublication', {'lang': 'DUTCH'})
    #
    # payloadPublication.set(ET.QName(XSI, 'type'), 'GenericPublication')

    return tree


def convert_dict_to_el_tree_working(dict: dict) -> ET.ElementTree:
    d2_root = D2LogicalModel()
    d2_root.exchange = Exchange()
    d2_root.exchange.supplierIdentification = InternationalIdentifier(country=CountryEnum.BE,
                                                                      nationalIdentifier="Vlaamse Overheid")

    XSI = 'http://www.w3.org/2001/XMLSchema-instance'

    ET.register_namespace('', 'http://datex2.eu/schema/2/2_0')
    #ET.register_namespace('xsd', 'http://www.w3.org/2001/XMLSchema')

    tree = ET.ElementTree(
        ET.Element('{http://datex2.eu/schema/2/2_0}d2LogicalModel', {'modelBaseVersion': '2'}))
    root = tree.getroot()

    exchange = ET.SubElement(root, 'exchange')
    supplierIdentification = ET.SubElement(exchange, 'supplierIdentification')
    country = ET.SubElement(supplierIdentification, 'country')
    country.text = CountryEnum.BE
    nationalIdentifier = ET.SubElement(supplierIdentification, 'nationalIdentifier')
    nationalIdentifier.text = 'Vlaamse Overheid'
    # payloadPublication = ET.SubElement(root, 'payloadPublication', {'lang': 'DUTCH'})
    #
    # payloadPublication.set(ET.QName(XSI, 'type'), 'GenericPublication')

    return tree


def convert_dict_to_el_tree_2(dict: dict) -> ET.ElementTree:
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

    return tree
