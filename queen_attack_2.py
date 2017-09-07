import sys

def CalculateQueenAttack(n, k, qPos, obstaclePosList):
    chessBoard = [[0 for x in range(n + 1)] for y in range(n + 1)]
    directionalArray = [-1, 0, 1]
    # Mark all the unreachable positions
    for obstaclePos in obstaclePosList:
        chessBoard[obstaclePos[0]][obstaclePos[1]] = 1

    counter = 0
    for factor in range(1, n):
        for x in directionalArray:
            for y in directionalArray:
                if(x == 0 and y == 0):
                    continue
                xIdx = (x * factor) + qPos[0]
                yIdx = (y * factor) + qPos[1]
                prevXIdx = (x * (factor - 1)) + qPos[0]
                prevYIdx = (y * (factor - 1)) + qPos[1]
                if(xIdx > n or xIdx < 1):
                    continue
                if(yIdx > n or yIdx < 1):
                    continue
                if(chessBoard[xIdx][yIdx] == 1):
                    continue
                elif(chessBoard[prevXIdx][prevYIdx] == 1):
                    chessBoard[xIdx][yIdx] = 1
                    continue
                counter = counter + 1

    return counter

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    qx, qy = input().strip().split(' ')
    queenPosition = (int(qx), int(qy))
    listOfObstacePositions = list()
    for obstacles in range(int(k)):
        x, y = input().strip().split(' ')
        listOfObstacePositions.append((int(x), int(y)))

    numberOfAttacks = CalculateQueenAttack(int(n), int(k), queenPosition, listOfObstacePositions)
    print(numberOfAttacks)