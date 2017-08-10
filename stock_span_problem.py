import sys

def CalculateStockSpan(array: list):
    stack = []
    stockSpan = []
    stack.append(0)
    stockSpan.append(1)
    for idx in range(1, len(array)):
        while(len(stack) > 0):
            stackPop = stack.pop()
            if(array[stackPop] > array[idx]):
                stack.append(stackPop)
                break
        value = idx + 1 if len(stack) == 0 else idx - stackPop
        stockSpan.append(value)
        stack.append(idx)
    return stockSpan

if __name__ == "__main__":
    noOfTestCases = int(input())
    for testCase in range(noOfTestCases):
        lengthOfArray = int(input())
        array = list(map(int, input().split()))
        for element in CalculateStockSpan(array):
            print(element, end=" ")
        print()
