import os
import re

def GetSuffixes(directoryPath: str):
    files = os.listdir(directoryPath)
    regexString = "Views\.V1\.OfficeExperience\.([a-z A-Z].*)\.resx"
    for file in files:
        regex_search = re.search(regexString, file)
        if regex_search:
            file_culture = regex_search.group(1)
            print("new CultureInfo(\"{}\"),".format(file_culture))

if __name__ == "__main__":
    directoryPath = str(input("Enter directory path: "))
    GetSuffixes(directoryPath)
