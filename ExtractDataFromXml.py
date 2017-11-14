import sys
import fileinput
import xml.etree.ElementTree as ET
import csv

def ParseXML(file_location):
    tree = ET.parse(file_location)
    root = tree.getroot()
    listOfData = list()
    for product in root.iter('Product'):
        product_config_name = product.attrib['ProductConfigName']
        pkpn = product.find('PKPN')
        version = product.attrib['Version']
        product_type = product.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"]
        # product_type = None
        # print(product.attrib)
        if(pkpn != None):
            data = (product_config_name, version, product_type, pkpn.text)
            listOfData.append(data)
    with open('OfferData.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ProductConfigName', 'Version', 'Type', 'PKPN'])
        for data in listOfData:
            writer.writerow(data)



if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Need the location of XML file")
    file_location = sys.argv[1]
    ParseXML(file_location)