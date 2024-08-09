import xml.etree.ElementTree as ET
from pathlib import Path

from converter import convert_json_to_xml


def test_convert():
    input_path = Path('truckparking20220516.json')
    output_path = Path('generated.xml')
    expected_path = Path('datex2truckparkings.xml')
    convert_json_to_xml(json_path=input_path, xml_path=output_path)

    result = ET.tostring(ET.parse(output_path).getroot())
    expected = ET.tostring(ET.parse(expected_path).getroot())

    assert expected == result
