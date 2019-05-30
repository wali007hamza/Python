import sys


def find_median(array1: list(), array2: list()):
    len1 = len(array1)
    len2 = len(array2)
    start1 = 0
    start2 = 0
    end1 = len(array1)
    end2 = len(array2)

    median1 = (len1 + len2)/2
    median2 = None
    if((len1 + len2)%2 == 1):
        median2 = median1


    while (start1 < end1 and start2 < end2):
        mid1 = binary_intersect(start1, end1)
        mid2 = binary_intersect(start2, end2)

        if(mid1 + mid2 + 1 > median1):
            if(array1[mid1] > array2[mid2]):
                end1 = mid1
            elif(array2[mid2] > array1[mid1]):
                end2 = mid2

        elif(mid1 + mid2 + 1 < median1):
            if(array1[mid1] < array2[mid2]):
                start1 = mid1
            elif(array2[mid2] < array1[mid1]):
                start2 = mid2

        if(mid1 + mid2 + 1 == median1):



def binary_intersect(lo: int, hi: int):
    return int((lo + hi) / 2)


if __name__ == "__main__":
    array1 = None
    array2 = None

    if (len(sys.argv) == 1):
        array1 = list(map(int, input().strip().split()))
        array2 = list(map(int, input().strip().split()))
    elif (len(sys.argv) == 3):
        array1 = list(map(int, sys.argv[1].split(",")))
        array2 = list(map(int, sys.argv[2].split(",")))
    else:
        raise Exception("Incorrect number of arguments")
    find_median(array1, array2)
