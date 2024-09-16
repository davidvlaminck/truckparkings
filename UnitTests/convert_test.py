import xml.etree.ElementTree as ET
from pathlib import Path
from freezegun import freeze_time

from converter import convert_json_to_xml, convert_dict_to_el_tree


def test_convert():
    input_path = Path('truckparking20220516.json')
    output_path = Path('generated.xml')
    expected_path = Path('datex2truckparkings.xml')
    convert_json_to_xml(json_path=input_path, xml_path=output_path)

    result = ET.tostring(ET.parse(output_path).getroot())
    expected = ET.tostring(ET.parse(expected_path).getroot())

    assert expected == result


def test_one_parking():
    output_path = Path('generated_one_parking.xml')
    expected_path = Path('one_parking.xml')
    data_dict = {'parkings': [{"parkingLocation": {
        "pointByCoordinates":
            {"pointCoordinates": {"latitude": 50.854082325888626, "longitude": 4.658283837917553}}},
        "parkingUsageScenario": {"parkingUsageScenario": "Snelwegparking",
                                 "truckParkingDynamicManagement": "noDynamicParkingManagement"},
        "parkingNumberOfSpaces": 270, "parkingAccess": {
            "accessCategory": "vehicle entrance",
            "id": "{1990A8C2-95D1-477B-8502-BAEE37A6265A}",
            "location": [{"pointByCoordinates": {
                "pointCoordinates": {
                    "latitude": 50.85247680655896,
                    "longitude": 4.661924219216416}}}],
            "PrimaryRoad": [{"roadIdentifier": "A3",
                             "nameOfRoad": "Liège-Brussel",
                             "distanceToThisRoad": "None",
                             "roadDestination": "Brussel"}]},
        "parkingEquipmentOrServiceFacility": [
            {"serviceFacilityType": "Shop", "type": "ServiceFacility"},
            {"serviceFacilityType": "Hotel", "type": "ServiceFacility"},
            {"serviceFacilityType": "Restaurant", "type": "ServiceFacility"},
            {"serviceFacilityType": "Petrol station", "type": "ServiceFacility"}],
        "parkingSiteAddress": None, "groupOfParkingSpaces": [{"parkingSpaceBasics": {
            "parkingTypeOfGroup": "statisticsOnly", "parkingNumberOfSpaces": 230,
            "assignedParkingAmongOthers": {"vehicleCharacteristics": {"vehicleType": "Car", "loadType": None}}}}, {
            "parkingSpaceBasics": {
                "parkingTypeOfGroup": "statisticsOnly",
                "parkingNumberOfSpaces": 34,
                "assignedParkingAmongOthers": {
                    "vehicleCharacteristics": {
                        "vehicleType": "Lorry",
                        "loadType": None}}}},
            {"parkingSpaceBasics": {
                "parkingTypeOfGroup": "statisticsOnly",
                "parkingNumberOfSpaces": 6,
                "assignedParkingAmongOthers": {
                    "vehicleCharacteristics": {
                        "vehicleType": "Bus",
                        "loadType": None}}}}],
        "interUrbanParkingSiteLocation": None,
        "operator": {"contactDetailsPostcode": None, "publishingAgreement": None,
                     "contactDetailsStreet": None, "contactOrganisationName": 3, "country": None,
                     "contactDetailsCity": None,
                     "contactDetailsEMail": "customerservice@gotexaco.com",
                     "contactDetailsTelephoneNumber": "",
                     "id": "3f2738f6-2da2-4215-9ead-53990b7489a6"},
        "parkingName": "E40 Heverlee Luik - Brussel",
        "tariffsAndPayment": {"freeOfCharge": None},
        "parkingStandardsAndSecurity": {"labelSecurityLevel": None,
                                        "labelSecurityLevelSelfAssessment": None,
                                        "certifiedSecureParking": None,
                                        "parkingSupervision": {"parkingSupervision": None},
                                        "parkingSecurity": [], "labelServiceLevel": None},
        "id": "c00134eb-dbd1-4b04-9b5d-a0834cc9193e"}]}
    with freeze_time("2024-01-01"):
        tree = convert_dict_to_el_tree(
            data_dict=data_dict,
            parking_table_id='1', version='3')
        tree.write(output_path, encoding='utf-8', xml_declaration=True)

    result = ET.parse(output_path).getroot()
    expected = ET.parse(expected_path).getroot()
    assert elements_equal(result, expected)


def test_empty_dict():
    output_path = Path('generated.xml')
    expected_path = Path('empty.xml')
    with freeze_time("2024-01-01"):
        tree = convert_dict_to_el_tree(data_dict={'parkings': []}, parking_table_id='1', version='1')
        tree.write(output_path, encoding='utf-8', xml_declaration=True)

    result = ET.parse(output_path).getroot()
    expected = ET.parse(expected_path).getroot()
    assert elements_equal(result, expected)


def elements_equal(e1, e2):
    if e1.tag != e2.tag: raise SyntaxError('tag not equal')
    e1_text = e1.text.strip() if e1.text else ''
    e2_text = e2.text.strip() if e2.text else ''
    if e1_text != e2_text: raise SyntaxError('text not equal')
    e1_tail = e1.tail.strip() if e1.tail else ''
    e2_tail = e2.tail.strip() if e2.tail else ''
    if e1_tail != e2_tail: raise SyntaxError('tail not equal')
    if e1.attrib != e2.attrib: raise SyntaxError('attrib not equal')
    if len(e1) != len(e2): raise SyntaxError('length not equal')
    return all(elements_equal(c1, c2) for c1, c2 in zip(e1, e2))
