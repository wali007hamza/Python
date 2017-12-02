import sys
import copy


def calculate_max_path(matrix, m, n):
    max_matrix = copy.deepcopy(matrix)
    for j in range(n):
        max_matrix[m - 1][j] = matrix[m - 1][j]
    for i in reversed(range(m - 1)):
        for j in range(m):
            if(j == 0):
                max_matrix[i][j] += max_matrix[i + 1][j + 1]
            elif(j == n - 1):
                max_matrix[i][j] += max_matrix[i + 1][j - 1]
            else:
                max_matrix[i][j] += max(max_matrix[i + 1][j + 1],
                                    max_matrix[i + 1][j - 1])
    max_sum = -sys.maxsize
    for j in range(n):
        if(max_matrix[0][j] > max_sum):
            max_sum = max_matrix[0][j]

    return max_sum, max_matrix

def find_max_path(max_matrix, max_sum, m, n):
    path = list()
    for j in range(n):
        if(max_matrix[0][j] == max_sum):
            path.append((0, j))
            break

    for i in range(1, m):
        last_i, last_j = path[len(path) - 1]
        if(last_j == n - 1):
            path.append((i, last_j - 1))
        elif(last_j == 0):
            path.append((i, last_j + 1))
        else:
            if(max_matrix[i][last_j-1] > max_matrix[i][last_j+1]):
                path.append((i, last_j-1))
            else:
                path.append((i, last_j+1))

    return path

if __name__ == "__main__":
    m, n = input().strip().split()
    m = int(m)
    n = int(n)
    matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        matrix[i] = list(map(int, input().strip().split()))
    max_sum, max_matrix = calculate_max_path(matrix, m, n)
    path = find_max_path(max_matrix, max_sum, m, n)
    print(path)

