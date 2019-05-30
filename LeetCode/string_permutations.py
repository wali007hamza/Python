import sys


def str_permutation(string: str, start: int, end: int):
    if (start >= end):
        print(string)
        return

    for i in range(start, end):
        transient_string = swap_chars(string, start, i)
        str_permutation(transient_string, start + 1, end)


def swap_chars(string: str, source: int, target: int):
    list_chars = [str(i) for i in string]
    temp_char = list_chars[source]
    list_chars[source] = list_chars[target]
    list_chars[target] = temp_char
    return "".join(list_chars)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Provide string in via the command line argument")
    string = str(sys.argv[1].strip())
    str_permutation(string, 0, len(string))
