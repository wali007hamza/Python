import sys
import math


class Solution:
    def convert(self, string, num_of_rows):
        str_len = len(string)
        arr_len = num_of_rows
        if(string == ''):
            return ''
        if(str_len == 1):
            return string
        if(num_of_rows == 1):
            return string
        temp = math.ceil(str_len / (2 * num_of_rows - 2))
        arr_width = temp * ((2 * num_of_rows - 2))
        zig_zag_map = [['' for y in range(0, arr_width)]
                       for x in range(0, arr_len)]

        i = 0
        j = 0
        stepper = (1, 0)
        str_itr = 0
        while(str_itr < str_len):
            if(i == arr_len - 1):
                stepper = (-1, 1)
            if(i == 0):
                stepper = (1, 0)
            zig_zag_map[i][j] = string[str_itr]
            str_itr += 1
            i += stepper[0]
            j += stepper[1]

        final_str = list()
        for x in range(0, arr_len):
            for y in range(0, arr_width):
                char = zig_zag_map[x][y]
                if(char != ''):
                    final_str.append(char)
        return ''.join(final_str)


if __name__ == "__main__":
    string = input().strip()
    num_of_rows = int(input())
    ret_value = Solution().convert(string, num_of_rows)
    print(ret_value)
