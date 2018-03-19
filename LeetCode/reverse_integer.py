import sys

class Solution:
    def reverse(self, number):
        if(number < 0):
            negative_number = True
            number *= -1
        else:
            negative_number = False

        num_str = str(number)
        rev_num_str = num_str[::-1]
        if(negative_number):
            rev_num_str = "-" + rev_num_str

        number = int(rev_num_str)
        if(number > 2**31 or number < -1*2**31):
            return 0

        return int(rev_num_str)

if __name__ == "__main__":
    number = int(input().strip())
    ret_value = Solution().reverse(number)
    print(ret_value)
