import sys


if __name__ == "__main__":
    array1 = None
    array2 = None

    if(len(sys.argv) == 1):
        array1 = list(map(int, input().strip().split()))
        array2 = list(map(int, input().strip().split()))
    elif(len(sys.argv) == 3):
        array1 = list(map(int, sys.argv[1].split(",")))
        array2 = list(map(int, sys.argv[2].split(",")))
    else:
        raise Exception("Incorrect number of arguments")

    print(array1, " ", array2)

