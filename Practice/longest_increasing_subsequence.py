import sys


def find_lis(array: list):
    max_reached = [0 for i in range(len(array))]
    max_reached_map = [-1 for i in range(len(array))]
    global_max = 0
    global_max_index = -1
    for i in range(len(array)):
        j = i - 1
        max_yet = 0
        while(j >= 0):
            if(array[i] >= array[j]):
                if(max_reached[j] >= max_yet):
                    max_reached_map[i] = j
                    max_yet = max_reached[j]
            max_reached[i] = max_yet + 1
            if(max_yet >= global_max):
                global_max = max_yet
                global_max_index = i

            j -= 1

    j = global_max_index
    lis = list()
    while(j >= 0):
        lis.append(array[j])
        j = max_reached_map[j]

    return lis


if __name__ == "__main__":
    array = list(map(int, input().strip().split()))
    lis = find_lis(array)
    print(lis)
