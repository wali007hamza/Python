import sys
from typing import List
from bisect import bisect

def search(array: list(), in_search: int) -> int:
    point_of_rotation = find_point_of_rotation(array)
    print(f'Point of Rotation: {point_of_rotation}, InSearch: {in_search}')

    lo = 0
    hi = len(array)
    if (array[lo] < in_search and array[point_of_rotation - 1] >= in_search):
        hi = point_of_rotation
    else:
        lo = point_of_rotation

    binary_search = bisect(array, in_search, lo, hi)
    return binary_search - 1


def find_point_of_rotation(array: List[int]) -> int:
    lo = 0
    hi = len(array)
    last_element = array[len(array) - 1]
    mid = None
    while (lo < hi):
        mid = int((lo + hi) / 2)
        if (array[mid - 1] > array[mid]):
            break
        # If the point in consideration is bigger than the last element, then the point of rotaton is towards the right
        if (array[mid] >= last_element):
            lo = mid + 1
        else:
            hi = mid - 1

    return mid


if __name__ == "__main__":
    array1 = None
    in_search = None

    if (len(sys.argv) == 1):
        array1 = list(map(int, input().strip().split()))
    elif (len(sys.argv) == 3):
        array1 = list(map(int, sys.argv[1].split(",")))
        in_search = int(sys.argv[2].strip())

    else:
        raise Exception("Incorrect number of arguments")
    search_index = search(array1, in_search)
    print(search_index)

