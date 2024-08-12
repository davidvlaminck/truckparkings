import xml.etree.ElementTree as ET
from pathlib import Path

from converter import convert_json_to_xml, convert_dict_to_el_tree


def test_convert():
    input_path = Path('truckparking20220516.json')
    output_path = Path('generated.xml')
    expected_path = Path('datex2truckparkings.xml')
    convert_json_to_xml(json_path=input_path, xml_path=output_path)

    result = ET.tostring(ET.parse(output_path).getroot())
    expected = ET.tostring(ET.parse(expected_path).getroot())

    assert expected == result


def test_empty_dict():
    output_path = Path('generated.xml')
    expected_path = Path('empty.xml')
    tree = convert_dict_to_el_tree(dict={})
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
