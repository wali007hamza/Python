import sys


class Solution:
    def longestPalindrome(self, s):
        str_len = len(s)
        dp_map = [[0 for y in range(0, str_len)] for x in range(0, str_len)]
        current_len = 0
        str_start = -1
        str_end = -1
        max_len = -1
        for i in range(0, str_len):
            dp_map[i][i] = 1
            current_len = 1
            if(current_len > max_len):
                str_start = i
                str_end = i
                max_len = current_len

        for window in range(2, str_len + 1):
            for i in range(0, str_len):
                j = i + window - 1
                if(j >= str_len):
                    continue
                if(window == 2):
                    if(s[i] == s[j]):
                        dp_map[i][j] = 2
                        current_len = 2
                        if(current_len > max_len):
                            max_len = current_len
                            str_start = i
                            str_end = j
                else:
                    if(s[i] == s[j] and dp_map[i+1][j-1] > 0):
                        dp_map[i][j] = dp_map[i+1][j-1] + 2
                        current_len = dp_map[i][j]
                        if(current_len > max_len):
                            max_len = current_len
                            str_start = i
                            str_end = j

        return s[str_start:str_end+1]


if __name__ == "__main__":
    string = input().strip()
    ret_value = Solution().longestPalindrome(string)
    print(ret_value)
