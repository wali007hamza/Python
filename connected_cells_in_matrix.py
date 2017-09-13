import sys

DIRECTIONAL_ARRAY= [-1, 0, 1]
def find_largest_forest_size(N, M, matrix):
    markingMatrix = list()
    for ni in range(N):
        mx = list()
        for mi in range(M):
            mx.append(0)
        markingMatrix.append(mx)

    largest_forest = -1
    for ni in range(N):
        for mi in range(N):
            if(markingMatrix[ni][mi] > 0):
                continue
            if(matrix[ni][mi] == 1):
                forest_size = dfs(N, M, ni, mi, matrix, markingMatrix) + 1
                largest_forest = forest_size if forest_size > largest_forest else largest_forest

    return largest_forest

def dfs(N, M, nx, mx, matrix, markingMatrix):
    counter = 0
    if(markingMatrix[nx][mx] == 2):
        return 0
    for i in DIRECTIONAL_ARRAY:
        for j in DIRECTIONAL_ARRAY:
            if(i == 0 and j == 0):
                continue

            pos_n = nx + i
            pos_m = mx + j
            if(pos_n < 0 or pos_n >= N or pos_m < 0 or pos_m >= M):
                continue

            if(markingMatrix[pos_n][pos_m] > 0):
                continue

            if(matrix[pos_n][pos_m] == 1):
                markingMatrix[nx][mx] = 2
                markingMatrix[pos_n][pos_m] = 1
                counter = counter + dfs(N, M, pos_n, pos_m, matrix, markingMatrix) + 1

    return counter;


if __name__ == "__main__":
    N = int(input().strip())
    M = int(input().strip())
    matrix = list()
    for ni in range(N):
        mi = list(map(int, input().strip().split()))
        matrix.append(mi)
    largest_forest = find_largest_forest_size(N, M, matrix)
    print(largest_forest)



