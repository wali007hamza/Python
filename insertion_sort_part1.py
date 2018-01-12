import sys


def insertion_sort(elements, should_print = False):
    n = len(elements)
    comparand = elements[n - 1]
    i = n - 1
    while(i >= 0):
        if(i == 0):
            elements[i] = comparand
        elif(elements[i - 1] > comparand):
            elements[i] = elements[i-1]
        else:
            elements[i] = comparand
            i = -2
        i = i - 1
        if(should_print):
            print(*elements, sep=' ')


if __name__ == "__main__":
    arraySize = input().strip(' ').split()
    elements = list(map(int, input().strip(' ').split()))
    insertion_sort(elements, should_print=True)
