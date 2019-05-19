import sys


def play1(array: list()):
    for num in array:
        print(num, " ")

if __name__ == "__main__":
    array = list()
    if(len(sys.argv) > 1):
        array = list(map(int, sys.argv[1].split(',')))
    else:
        array = list(map(int, input().split()))
    play1(array)