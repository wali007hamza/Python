import sys

def find_number_of_pairs(N, K, numbers):
    sortedNumbers = sorted(numbers)
    i = 0
    j = 0
    count = 0
    while(j < N and i < N):
        if(sortedNumbers[j] - sortedNumbers[i] < K):
            j = j + 1
        elif(sortedNumbers[j] - sortedNumbers[i] > K):
            i = i + 1
        elif(sortedNumbers[j] - sortedNumbers[i] == K):
            j = j + 1
            count = count + 1

    return count

if __name__ == "__main__":
    N,K= input().strip().split(' ')
    numbers = list(map(int, input().strip().split(' ')))
    print(find_number_of_pairs(len(numbers), int(K), numbers))
