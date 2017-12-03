import sys


def print_fib(n: int):
    return None

def find_fib(n: int):
    fib = list()
    fib.append(0)
    fib.append(1)
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 100)

    return fib


def find_pattern(fibs: list):
    already_encountered = dict()
    for i in range(len(fibs)):
        key = str(fibs[i]) + "_" + str(fibs[i + 1])
        if(key in already_encountered):
            return i
        else:
            already_encountered[key] = 1

    return 0

def find_last_two_digits(fibs: list, n: int):
    return fibs[n % 300]

if __name__ == "__main__":
    fibs =find_fib(302)
    rep_n = find_pattern(fibs)
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        print(find_last_two_digits(fibs, n))

