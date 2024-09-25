from pathlib import Path

from converter import convert_json_to_xml
from generated_classes import D2LogicalModel

import xmlschema


# https://stackoverflow.com/questions/299588/validating-with-an-xml-schema-in-python
if __name__ == '__main__':
    input_path = Path('truckparking20240722.json')
    output_path = Path('generated_20240722.xml')

    convert_json_to_xml(json_path=input_path, xml_path=output_path)

    try:
        xmlschema.validate("generated_20240722", "DATEXIISchema_2_2_3.xsd")
        print('valid XML')
    except Exception as ex:
        print(ex)

# lxml
