import sys


N = 100000

def factors_sum(sieve: list(), n: int):
    return sieve[n]


def find_sieve_eratosthenes(n: int):
    sieve = [1 for i in range(n)]
    for i in range(2, n):
        j = i
        while(j < n):
            sieve[j] += i
            j += i

    return sieve


if __name__ == "__main__":
    number = int(input().strip())
    sieve = find_sieve_eratosthenes(N)
    fact_sum = factors_sum(sieve, number)
    print(fact_sum)
