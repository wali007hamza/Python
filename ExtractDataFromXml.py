import sys
import fileinput
import xml.etree.ElementTree as ET
import csv


def ParseXML(file_location):
    tree = ET.parse(file_location)
    root = tree.getroot()
    listOfData = list()
    for offer_package in root.iter('OfferPackage'):
        offer_id = offer_package.attrib['OfferId']
        product_groups = offer_package.find('ProductGroups')
        for product_group in product_groups.iter('ProductGroup'):
            category = product_group.attrib['Category']
            for product in product_groups.iter('Product'):
                product_config_name = product.attrib['ProductConfigName']
                pkpn = product.find('PKPN')
                version = product.attrib['Version']
                product_type = product.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"]
                if(pkpn != None):
                    data = (offer_id, category, product_config_name,
                            version, product_type, pkpn.text)
                    listOfData.append(data)
    with open('OfferData.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ['OfferId', 'Category', 'ProductConfigName', 'Version', 'Type', 'PKPN'])
        for data in listOfData:
            writer.writerow(data)


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Need the location of XML file")
    file_location = sys.argv[1]
    ParseXML(file_location)
