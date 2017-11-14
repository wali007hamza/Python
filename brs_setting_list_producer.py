import fileinput
import re
import uuid

def GenerateBrsSetting(template, noOfSettings: int, entity_prefix: str):
    positionalArray = GetAlphaNumericPositionalArray()
    batchSize = int(len(positionalArray) / noOfSettings) + 2
    idx = 0
    settingsArray = []
    while(idx < len(positionalArray) - batchSize):
        settingsArray.append(template.format(FriendlyNameSuffix=positionalArray[idx], CorrelationId=uuid.uuid4(), PartitionKeyLowerBound="{}_{}".format(
            entity_prefix, positionalArray[idx]), PartitionKeyUpperBound="{}_{}".format(
                entity_prefix, positionalArray[idx + batchSize - 1])))
        idx = idx + batchSize - 1

    settingsArray.append(template.format(
        FriendlyNameSuffix=positionalArray[idx],
        CorrelationId=uuid.uuid4(),
        PartitionKeyLowerBound="{}_{}".format(entity_prefix, positionalArray[idx]),
        PartitionKeyUpperBound="{}_{}".format(entity_prefix, positionalArray[len(positionalArray) - 1])))

    return settingsArray


def GetAlphaNumericPositionalArray():
    positionalArray = [chr(char) for char in range(ord('0'), ord('9') + 1)]
    positionalArray.extend([chr(char)
                            for char in range(ord('a'), ord('f') + 1)])
    return positionalArray


def WriteToFile(settingsArray):
    file = open("BrsSettings.txt", "w")
    file.write("\n".join(settingsArray))
    file.close()


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

    settingsArray = GenerateBrsSetting(template, numberOfSettings, "EWW")
    WriteToFile(settingsArray)
