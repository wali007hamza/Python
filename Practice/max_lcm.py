import sys


primes = []

def create_sieve(n: int):
    sieve = [0 for i in range(n)]
    primes = list()
    for i in range(2, n):
        if(sieve[i] == 0):
            primes.append(i)
            j = i
            while(j < n):
                sieve[j] = 1
                j += i

    return primes, sieve


def lcm(a: int, b: int):
    product = a * b
    hcf = gcd(a,b)
    return int(product / hcf)

def composite_lcm(*nums):
    lcm_val = nums[0]
    for i in range(1, len(nums)):
        lcm_val = lcm(lcm_val, nums[i])

    return lcm_val


def gcd(a: int, b: int):
    while b:
        a, b = b, a%b

    return a


def find_largest_lcm(n: int):
    for

if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        val = find_largest_lcm(n)
        print(val)
