import sys

def FindDuplicate(listOfNumbers):
    xorResultArrayMembers = 0
    xorResultN = 0
    for idx in range(1, len(listOfNumbers) + 1):
        xorResultArrayMembers ^= listOfNumbers[idx - 1]
        xorResultN ^= idx

    xorCombined = xorResultN ^ xorResultArrayMembers
    lsb = xorCombined & ~(xorCombined - 1)
    xor1 = 0
    xor2 = 0
    for idx in range(1, len(listOfNumbers) + 1):
        if(listOfNumbers[idx - 1] & lsb):
            xor1 ^= listOfNumbers[idx - 1]
        else:
            xor2 ^= listOfNumbers[idx - 1]

        if(idx & lsb):
            xor1 ^= idx
        else:
            xor2 ^= idx

    # Find the number
    for number in listOfNumbers:
        if(number == xor1):
            return xor1

    return xor2

if __name__ == "__main__":
    testCases = int(input().strip())
    for testCase in range(testCases):
        listOfNumbers = list(map(int, input().strip().split()))
        duplicateNumber = FindDuplicate(listOfNumbers)
        print(duplicateNumber)
