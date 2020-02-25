import sys

if __name__ == "__main__":
    (m,n) = tuple(map(int, input().strip().split(",")))
    matrix = list()
    for _ in range(m):
        row = list(map(int, input().strip().split(",")))
        matrix.append(row)

    print(matrix)
