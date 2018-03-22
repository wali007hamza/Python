# Understood the problem incorrectly. The problem that I assumed was more difficult and the solution that I came up with was pretty darn good

import sys


class Solution:
    def maxArea(self, heights):
        arr_len = len(heights)
        stack = list()
        stack.append((0, heights[0]))
        i = 1
        max_height = -1
        while(i < arr_len and len(stack) >= 0):
            curr_height = 0
            if(len(stack) == 0):
                stack.append((i, heights[i]))
                i += 1
                continue

            j_index, j_height = stack.pop()
            if(j_height < heights[i]):
                curr_height = (i - j_index) * j_height
                max_height = max(curr_height, max_height)
                continue

            elif(j_height >= heights[i]):
                curr_height = (i - j_index) * heights[i]
                max_height = max(curr_height, max_height)
                stack.append((j_index, j_height))
                if(j_height != heights[i]):
                    stack.append((i, heights[i]))
                i += 1

            # print(max_height, " ", i," ", j_index)

        return max_height


if __name__ == "__main__":
    heights = list(map(int, input().strip().split()))
    ret_value = Solution().maxArea(heights)
    print(ret_value)
