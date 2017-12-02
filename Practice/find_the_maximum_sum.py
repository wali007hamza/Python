import sys


mod_val = 10e8 + 7

def find_max_sum(numbers: list):
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    positive_numbers = list(filter(lambda x: x >= 0, numbers))

    negative_numbers = sorted(negative_numbers, reverse=True)
    positive_numbers = sorted(positive_numbers, reverse=False)
    max_sum = 0
    while(True):
        x = 0
        y = 1
        if(len(negative_numbers) > 0):
            x = negative_numbers.pop()
        else:
            break
        if(len(negative_numbers) > 0):
            y = negative_numbers.pop()
        else:
            negative_numbers.append(x)
            break
        max_sum += x * y

    if(len(negative_numbers) > 0):
        # new_list = list()
        # new_list.append(negative_numbers.pop())
        positive_numbers = [negative_numbers.pop()] + positive_numbers

    while(True):
        x = 0
        y = 1
        if(len(positive_numbers) > 0):
            x = positive_numbers.pop()
        else:
            break
        if(len(positive_numbers) > 0):
            y = positive_numbers.pop()
        max_sum += x * y

    return max_sum


if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        numbers = list(map(int, input().strip().split()))
        max_sum = find_max_sum(numbers)
        if(max_sum > 0):
            max_sum %= mod_val
        print(int(max_sum))
