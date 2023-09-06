# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        output = 0
        odd_present = False
        for char, value in char_count.items():
            if value % 2 == 0:
                output += value
            else:
                odd_present = True
                output += value - 1
                
        if odd_present:
            output += 1
        return output

                