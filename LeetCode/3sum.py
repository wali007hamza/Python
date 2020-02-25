import sys


class Solution():
    def threeSum(self, nums):
        arr_len = len(nums)
        nums = sorted(nums)
        triplets = set()
        triplets_list = list()
        for i in range(0, arr_len):
            should_exit = 0
            j = i + 1
            k = arr_len - 1
            while (j < k):
                current_sum = nums[i] + nums[j] + nums[k]
                if (current_sum == 0):
                    map_key = "{a} {b} {c}".format(
                        a=str(nums[i]), b=nums[j], c=nums[k])
                    if (not (map_key in triplets)):
                        triplets.add(map_key)
                        triplets_list.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                elif (current_sum > 0):
                    k = k - 1
                else:
                    j = j + 1
                if (nums[i] == nums[j] and nums[j] == nums[k]
                        and nums[i] == nums[k]):
                    should_exit += 1
                if (should_exit > 2):
                    break
            if (should_exit > 2):
                break

        return triplets_list


if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    ret_value = Solution().threeSum(nums)
    print(ret_value)
