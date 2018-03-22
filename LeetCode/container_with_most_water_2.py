import sys


class Solution:
    def maxArea(self, heights):
        arr_len = len(heights)
        i = 0
        j = arr_len - 1
        max_area = -1
        while(i <= j):
            current_area = min(heights[i], heights[j])*(j-i)
            if(heights[i] >= heights[j]):
                j -= 1
            else:
                i += 1
            max_area = max(max_area, current_area)

        return max_area


if __name__ == "__main__":
    heights = list(map(int, input().strip().split()))
    ret_value = Solution().maxArea(heights)
    print(ret_value)