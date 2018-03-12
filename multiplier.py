import sys


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise AttributeError("Need to specify 2 arguments")

    print(int(sys.argv[1]) * int(sys.argv[2]))