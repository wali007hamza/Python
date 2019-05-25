import sys
from typing import List, Tuple
from bisect import bisect, bisect_left, bisect_right


def search_range(nums: List[int], target: int) -> Tuple:
    left_search = bisect_left(nums, target, 0, len(nums))
    right_search = bisect_right(nums, target, 0, len(nums))
    return (left_search, right_search -1)


if __name__ == "__main__":
    array = None
    in_search = None

    if (len(sys.argv) == 1):
        array = list(map(int, input().strip().split()))
    elif (len(sys.argv) == 3):
        array = list(map(int, sys.argv[1].split(",")))
        in_search = int(sys.argv[2].strip())

    else:
        raise Exception("Incorrect number of arguments")
    search_tuple = search_range(array, in_search)
    print(search_tuple[0], ' ', search_tuple[1])