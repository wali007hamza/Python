import sys


def print_number_possibilities(input_number, pos, number_map):
    if(pos >= len(input_number)):
        return ['']
    previous_permutations = print_number_possibilities(input_number, pos + 1, number_map)
    new_permutations = list()
    current_char = input_number[pos]
    print(current_char, " ", number_map[current_char])
    for char in number_map[current_char]:
        for previous_permutation in previous_permutations:
            new_permutations.append(char + previous_permutation)

    return new_permutations


if __name__ == "__main__":
    number = str(input().strip())
    number_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    print(print_number_possibilities(number, 0, number_map))
