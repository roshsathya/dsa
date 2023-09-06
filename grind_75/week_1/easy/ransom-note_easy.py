# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_dict = {}
        total_chars = 0

        for char in ransomNote:
            if char not in char_dict:
                char_dict[char] = 0
                total_chars += 1
            char_dict[char] += 1
        
        for char in magazine:
            if total_chars == 0:
                return True
            if char not in char_dict:
                continue
            char_dict[char] -= 1
            if char_dict[char] == 0:
                total_chars -= 1
        
        return bool(total_chars == 0)