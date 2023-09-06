# https://leetcode.com/problems/backspace-string-compare/

from collections import deque

class Solution:

    def get_string(self, s):
        stack = deque()
        idx = 0
        while idx < len(s):
            if s[idx] == "#":
                if len(stack):
                    stack.pop()
            else:
                stack.append(s[idx])
            idx += 1
        
        stack_len = len(stack)
        string_s = [None for i in range(stack_len)]
        while True:
            try:
                current_value = stack.pop()
            except:
                break
            stack_len -= 1
            string_s[stack_len] = current_value

        return "".join(string_s)

    def backspaceCompare(self, s: str, t: str) -> bool:
            string_s = self.get_string(s)
            string_t = self.get_string(t)
            return string_s == string_t