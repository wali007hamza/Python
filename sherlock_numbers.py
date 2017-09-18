import sys
from array import array

def sherlock_element_exists(array_a):
    n = len(array_a)
    array_sum_forward = array("i")
    element_sum = 0
    for number in array_a:
        element_sum = element_sum + number
        array_sum_forward.append(element_sum)

    element_sum = 0
    array_sum_reverse = array("i")
    idx = n - 1
    while(idx >= 0):
        element_sum = element_sum + array_a[idx]
        array_sum_reverse.append(element_sum)
        idx = idx - 1

    idx = 0
    exists = False
    for idx in range(n):
        if(array_sum_forward[idx] == array_sum_reverse[n - idx - 1] and array_sum_forward[idx] != 0):
            exists = True
            break

    return "YES" if exists else "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for testCase in range(t):
        n = int(input().strip())
        array_n = list(map(int, input().strip().split(' ')))
        print(sherlock_element_exists(array_n))
