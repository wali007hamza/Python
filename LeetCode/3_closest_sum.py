import sys


class Solution():
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        nums_len = len(nums)
        min_sum = sys.maxsize
        closest_sum = 0
        found_solution = False
        for i in range(0, nums_len):
            if(found_solution == True):
                break

            j = i + 1
            k = nums_len - 1
            while(j < k and found_solution == False):
                current_sum = nums[i] + nums[j] + nums[k]
                current_diff = abs(target-current_sum)
                min_sum = min(min_sum, current_diff)
                if(min_sum == current_diff):
                    closest_sum = current_sum
                if(current_sum > target):
                    k -= 1
                elif(current_sum < target):
                    j += 1
                else:
                    found_solution = True

        return closest_sum


if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    target = int(input())
    ret_value = Solution().threeSumClosest(nums, target)
    print(ret_value)
