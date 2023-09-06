# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = {}

        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
        
        for char in t:
            if char not in char_dict:
                return False
            if char_dict.get(char) == 0:
                return False
            char_dict[char] -= 1
        
        return True