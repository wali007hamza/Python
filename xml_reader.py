import sys
from lxml import etree
from xml.dom import minidom


def find_pkpns(pkpnObjectList):
    pkpnsList = []
    for pkpn in pkpnObjectList:
        pkpnsList.append(pkpn.firstChild.nodeValue)

    print("Is Unique" if are_elements_unique(pkpnsList) else "Not Unique")
    print(find_duplicates(pkpnsList))

def are_elements_unique(pkpnList):
    pkpnSet = set(pkpnList)
    if(len(pkpnList) == len(pkpnSet)):
        return True
    else:
        print(len(pkpnList))
        print(len(pkpnSet))
        return False

def find_duplicates(pkpnList):
    sortedList = sorted(pkpnList)
    lastPkpn = None
    duplicatesList = []
    for pkpn in sortedList:
        if(lastPkpn == pkpn):
            duplicatesList.append(pkpn)
        else:
            lastPkpn = pkpn

    return duplicatesList

if __name__ == "__main__":
    xml_file_name = None
    if(len(sys.argv) > 1):
        xml_file_name = sys.argv[1]
    else:
        xml_file_name = input().strip()

    doc = minidom.parse(xml_file_name)
    pkpnList = doc.getElementsByTagName('PKPN')
    find_pkpns(pkpnList)
