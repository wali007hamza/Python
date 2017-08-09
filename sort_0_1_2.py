import sys

def Sorter(listOfNumbers):
    mapOfNumbers = [0, 0 ,0]
    for num in listOfNumbers:
        if(num == 0):
            mapOfNumbers[0] = mapOfNumbers[0]+1
        if(num == 1):
            mapOfNumbers[1] = mapOfNumbers[1]+1
        if(num == 2):
            mapOfNumbers[2] = mapOfNumbers[2]+1

    tracker = 0
    for num in mapOfNumbers:
        for times in range(0, num):
            print(tracker, end=" ")
        tracker = tracker + 1

if __name__ == "__main__":
    testCases = int(input())
    for testCase in range(testCases):
        lengthOfArray = int(input())
        Sorter(list(map(int, input().split())))
        print()
