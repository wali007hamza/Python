import sys

def FindMissingNumbers(n, arrayN, m, arrayM):
    minNumN = FindMinNumber(arrayN)
    minNumM = FindMinNumber(arrayM)
    minNum = minNumN if minNumN < minNumM else minNumM

    listN = list()
    for idx in range(0, 100):
        listN.append(0)
    for number in arrayN:
        listN[number - minNum] = listN[number - minNum] + 1

    listM = list()
    for idx in range(0, 100):
        listM.append(0)
    for number in arrayM:
        listM[number - minNum] = listM[number - minNum] + 1


    missingNumbers = list()
    for idx in range(0, 100):
        if(listN[idx] != listM[idx]):
            missingNumbers.append(minNum + idx)

    return missingNumbers

def FindMinNumber(array):
    minNum = sys.maxsize
    for number in array:
        minNum = number if number < minNum else minNum
    return minNum

if __name__ == "__main__":
    n = int(input().strip())
    arrayN = list(map(int, input().strip().split()))
    m = int(input().strip())
    arrayM = list(map(int, input().strip().split()))
    missingNumbers = FindMissingNumbers(n, arrayN, m, arrayM)
    for number in missingNumbers:
        print(number, end=" ")