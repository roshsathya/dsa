# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx = 0
        last_idx = len(s)-1

        while idx < last_idx:
            if not s[idx].isalnum():
                idx += 1
                continue
            if not s[last_idx].isalnum():
                last_idx -= 1
                continue
            if s[idx].lower() != s[last_idx].lower():
                return False
            idx += 1
            last_idx -= 1
        return True