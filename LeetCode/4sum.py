import sys

class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        nums_len = len(nums)
        for i in range(0, nums_len):



if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    target = input().strip()
    ret_value = Solution().fourSum(nums, target)