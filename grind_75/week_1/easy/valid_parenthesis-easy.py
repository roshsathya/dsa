# url - https://leetcode.com/problems/valid-parentheses/

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for curr_bracket in s:
            if curr_bracket in ['(', '{', '[']:
                stack.append(curr_bracket)
            else:
                if not len(stack):
                    return False
                top_bracket = stack.pop()
                if top_bracket == '(' and curr_bracket != ')':
                    return False
                if top_bracket == '{' and curr_bracket != '}':
                    return False
                if top_bracket == '[' and curr_bracket != ']':
                    return False
        if len(stack):
            return False
        return True