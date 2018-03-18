import sys

class Solution:
    def isPalindrome(self, number):
        num_str = str(number)
        num_len = len(num_str)
        i = 0
        j = 0
        factor = int(num_len / 2)
        if(num_len % 2 == 0):
            i = factor - 1
            j = factor
        else:
            i = factor - 1
            j = factor + 1
        while(i >= 0 and j < num_len):
            if(num_str[i] != num_str[j]):
                return False
            else:
                i -= 1
                j += 1

        return True

if __name__ == "__main__":
    number = int(input().strip())
    ret_value = Solution().isPalindrome(number)
    print(ret_value)