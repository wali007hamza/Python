import sys

def QuickSort(array: list, start: int, end: int):
    if(start >= end):
        return
    pivot = ArrayPartition(array, start, end)
    QuickSort(array, start, pivot -1)
    QuickSort(array, pivot + 1, end)
    return


def ArrayPartition(array: list , start: int, end: int):
    pivot = end
    i = start
    j = pivot - 1
    while(i <= j):
        if(array[i] > array[pivot]):
            if(array[j] <= array[pivot]):
                Swap(array, i, j)
            if(array[j] >= array[pivot]):
                j = j - 1
        else:
            i = i + 1
    Swap(array, i, pivot)
    return i


def Swap(array: list, idx1: int, idx2: int):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp
    return


if __name__ == "__main__":
    noOfTestCases = int(input())
    for testCase in range(noOfTestCases):
        lengthOfArray = int(input())
        array = list(map(int, input().split()))
        QuickSort(array, 0, lengthOfArray - 1)
        for value in array:
            print(value, end=" ")
        print()