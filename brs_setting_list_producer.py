import fileinput
import re
import uuid


def GenerateBrsSetting(template, noOfSettings: int):
    positionalArray = GetAlphaNumericPositionalArray()
    batchSize = int(len(positionalArray) / noOfSettings) + 2
    idx = 0
    settingsArray = []
    while(idx < len(positionalArray) - batchSize):
        settingsArray.append(template.format(CorrelationId=uuid.uuid4(), PartitionKeyLowerBound="CWW_{}".format(positionalArray[idx]), PartitionKeyUpperBound="CWW_{}".format(positionalArray[idx + batchSize - 1])))
        idx = idx + batchSize - 1

    settingsArray.append(template.format(CorrelationId=uuid.uuid4(),
        PartitionKeyLowerBound="CWW_{}".format(positionalArray[idx]),
        PartitionKeyUpperBound="CWW_{}".format(positionalArray[len(positionalArray) - 1])))

    return settingsArray


def GetAlphaNumericPositionalArray():
    positionalArray = [chr(char) for char in range(ord('a'), ord('z') + 1)]
    positionalArray.extend([chr(char) for char in range(ord('0'), ord('9') + 1)])
    return positionalArray


if __name__ == "__main__":
    numberOfSettings = 0
    template = ""
    for line in fileinput.input():
        text = re.sub("\n", "", line)
        text = re.sub(" ", "", text)
        text = text.strip()
        if(not(text.isspace())):
            if(text.startswith("MaxNumberOfSettings")):
                numberOfSettings = int(text.split(":")[1])
            if(text.startswith("Template")):
                template = text.split("Template:")[1]

    settingsArray = GenerateBrsSetting(template, numberOfSettings)
    print("\n".join(settingsArray))