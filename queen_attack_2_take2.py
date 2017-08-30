import sys
import math

def CalculateQueenAttack(n, k, qPos, obstaclePosList):
    # directionalFactorsList = [[0 for x in range(3)] for y in range(3)
    directionalFactorsMap = {}
    directionalArray = [-1, 0, 1]
    for y in directionalArray:
        for x in directionalArray:
            if(x == 0 and y == 0):
                continue
            if(x != 0 and y != 0):
                yValue = n - qPos[0] if y >= 0 else qPos[0] - 1
                xValue = n - qPos[1] if x >= 0 else qPos[1] - 1
                directionalFactorsMap[GetDirectionalMapKey(y, x)] = min(yValue, xValue)
            if(x == 0 and y != 0):
                yValue = n - qPos[0] if y >= 0 else qPos[0] - 1
                directionalFactorsMap[GetDirectionalMapKey(y, x)] = yValue
            if(y == 0 and x != 0):
                xValue = n - qPos[1] if x >= 0 else qPos[1] - 1
                directionalFactorsMap[GetDirectionalMapKey(y, x)] = xValue

    for obstaclePos in obstaclePosList:
        y = obstaclePos[0] - qPos[0]
        x = obstaclePos[1] - qPos[1]
        factor = 1
        if(x == 0 and y != 0):
            factor = abs(y)
        if(y == 0 and x != 0):
            factor = abs(x)
        if(x != 0 and y != 0):
            if(abs(x) != abs(y)):
                continue
            factor = abs(x)

        yPos = y/factor
        xPos = x/factor
        factor = factor - 1
        currentFactorValue = directionalFactorsMap[GetDirectionalMapKey(int(yPos), int(xPos))]
        if(currentFactorValue is None):
            continue
        directionalFactorsMap[GetDirectionalMapKey(int(yPos),int(xPos))] = factor if factor < currentFactorValue else currentFactorValue

    counter = 0
    for key, value in directionalFactorsMap.items():
        counter = counter + value

    return counter

def GetDirectionalMapKey(y, x):
    return "{y}_{x}".format(y=y, x=x)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    qy, qx = input().strip().split(' ')
    queenPosition = (int(qy), int(qx))
    listOfObstacePositions = list()
    for obstacles in range(int(k)):
        y, x = input().strip().split(' ')
        listOfObstacePositions.append((int(y), int(x)))

    numberOfAttacks = CalculateQueenAttack(int(n), int(k), queenPosition, listOfObstacePositions)
    print(numberOfAttacks)