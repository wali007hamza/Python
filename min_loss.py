import sys
from bisect import bisect_left


def MinLoss(prices):
    indexedPrices = list()
    idx = 0
    for price in prices:
        indexedPrices.append((price, idx))
        idx = idx + 1

    sortedIndexedPrices = sorted(indexedPrices, key=lambda tup: tup[0])
    sortedPrices, indexes = zip(*sortedIndexedPrices)
    minLoss = sys.maxsize
    for priceIdx in range(0, len(prices)):
        pricePos = bisect_left(sortedPrices, prices[priceIdx])
        justSmallerPricePos = pricePos - 1
        if(justSmallerPricePos < 0):
            continue
        if(indexes[pricePos] < indexes[justSmallerPricePos]):
            loss = sortedPrices[pricePos] - sortedPrices[justSmallerPricePos]
            if(minLoss > loss):
                minLoss = loss

    return minLoss


if __name__ == "__main__":
    numberOfYears = int(input().strip())
    prices = list(map(int, input().split()))
    result = MinLoss(prices)
    print(result)
