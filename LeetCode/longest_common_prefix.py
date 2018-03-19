import sys


class Solution:
    def longestCommonPrefix(self, strings):
        if(len(strings) == 0):
            return ''
        min_string_length = min(len(string) for string in strings)
        i = 0
        is_common = True
        while(i < min_string_length and is_common):
            prev_string_char = None
            for string in strings:
                if(prev_string_char and string[i] != prev_string_char):
                    print("HI", " ", prev_string_char)
                    is_common = False
                    break
                else:
                    prev_string_char = string[i]
            if(is_common):
                i += 1

        return strings[0][:i]


if __name__ == "__main__":
    num_of_str = int(input().strip())
    strings = list()
    for i in range(0, num_of_str):
        strings.append(input().strip())

    ret_value = Solution().longestCommonPrefix(strings)
    print(ret_value)
