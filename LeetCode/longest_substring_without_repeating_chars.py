import sys


class Solution:

    def initializeArray(self):
        # try using hash map instead
        return [-1 for x in range(0, 100)]

    def lengthOfLongestSubstring(self, s):
        longest_substring = 0
        char_map = self.initializeArray()
        current_len = 0
        start_pos = 0
        for i in range(0, len(s)):
            if(char_map[ord(s[i]) - ord('0')] < start_pos):
                current_len += 1
                char_map[ord(s[i])- ord('0')] = i
            else:
                if(current_len > longest_substring):
                    longest_substring = current_len
                current_len = i - char_map[ord(s[i]) - ord('0')]
                start_pos = char_map[ord(s[i]) - ord('0')] + 1
                char_map[ord(s[i]) - ord('0')] = i

        if(current_len > longest_substring):
            longest_substring = current_len

        return longest_substring


if __name__ == "__main__":
    string = input().strip()
    print(Solution().lengthOfLongestSubstring(string))
