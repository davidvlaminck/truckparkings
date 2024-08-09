import xmlschema


# https://stackoverflow.com/questions/299588/validating-with-an-xml-schema-in-python
if __name__ == '__main__':
    try:
        xmlschema.validate("UnitTests/datex2truckparkings.xml", "DATEXIISchema_2_2_3.xsd")
        print('valid XML')
    except Exception as ex:
        print(ex)
