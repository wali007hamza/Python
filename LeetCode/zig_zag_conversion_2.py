import sys


class Solution:
    def convert(self, string, num_of_rows):
        window = num_of_rows + (num_of_rows - 2)
        padded_string = string + " " * window
        str_len = len(padded_string)
        if(window == 0):
            return string

        final_str = list()
        for k in range(0, num_of_rows):
            i = k
            j = window - k
            while(i < str_len and j < str_len):
                current_char = padded_string[i]
                if(current_char != " "):
                    final_str.append(current_char)
                i += window
                if(k != 0 and k != num_of_rows - 1):
                    current_char = padded_string[j]
                    if(current_char != " "):
                        final_str.append(current_char)
                    j += window

        return ''.join(final_str)


if __name__ == "__main__":
    string = input().strip()
    num_of_rows = int(input())
    ret_value = Solution().convert(string, num_of_rows)
    print(ret_value)
