# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        is_unique = True
        start = 0
        end = 0
        output = 0

        while end < len(s):
            if is_unique:
                current_char = s[end]
                char_dict[current_char] = char_dict.get(current_char, 0) + 1
                if char_dict[current_char] > 1:
                    is_unique = False
                    output = max(output, end-start)
                end += 1
            else:
                current_char = s[start]
                char_dict[current_char] -= 1
                if char_dict[current_char] == 1:
                    is_unique = True
                start += 1

        if is_unique:
            output = max(output, end-start)

        return output