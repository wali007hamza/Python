import sys
import bisect

def binary_search(numbers: list, item: int, lo: int, hi: int):
    i = bisect.bisect(numbers, item, lo, hi)
    if(numbers[i-1] == item):
        return i-1
    else:
        return -1


def two_sum(numbers: list, target: int):
    numbers_count = len(numbers)
    indexed_numbers = list()
    for i in range(0, numbers_count):
        indexed_numbers.append((i, numbers[i]))

    sorted_indexed_numbers = sorted(indexed_numbers, key=lambda tup: tup[1])

    indexes, sorted_numbers = zip(*sorted_indexed_numbers)
    for i in range(0, numbers_count):
        number_to_find = target - sorted_numbers[i]
        found_index = binary_search(sorted_numbers, number_to_find, i, numbers_count)
        if(found_index > 0):
            return [indexes[i], indexes[found_index]]


if __name__ == "__main__":
    numbers = list(map(int, input().strip().split()))
    target = int(input().strip())
    return_array = two_sum(numbers, target)
    print(return_array)
