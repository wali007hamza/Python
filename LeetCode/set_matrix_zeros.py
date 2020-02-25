import sys
from typing import List


class Solution:
    def setZeros(self, matrix: List[List[int]]):



if __name__ == "__main__":
    m,n = (map(int, input().split(",")))
    matrix = list()
    for i in range(m):
        row = list(map(int, input().strip().split(",")))
        matrix.append(row)

    print(matrix)



