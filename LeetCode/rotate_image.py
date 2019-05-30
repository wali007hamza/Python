import sys


def matrix_transpose(matrix, n: int, m: int):
    for i in range(n):
        for j in range(m):
            temp = matrix[i][j]
            if("-" in temp):
                continue
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = "-" + temp

    for i in range(n):
        for j in range(m):
            val = matrix[i][j]
            if("-" in val):
                matrix[i][j] = val[val.find("-") + 1:]
    return matrix

def reverse_rows(matrix, n: int):
    for i in range(n):
        curr_row = matrix[i]
        matrix[i] = [j for j in reversed(curr_row)]

    print(matrix)

if __name__ == "__main__":
    dimension = int(input().strip())
    matrix = [0 * dimension for i in range(dimension)]
    for i in range(dimension):
        row = input().strip().split(",")
        matrix[i] = row

    transposed_matrix = matrix_transpose(matrix, dimension, dimension)
    reverse_rows(transposed_matrix, dimension)
