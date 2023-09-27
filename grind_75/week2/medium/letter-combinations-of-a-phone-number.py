# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import string, math

class Solution:

    def helper(self, values, idx):
        if idx >= len(values):
            return [[]]
        output = []
        for digit in values[idx]:
            result = self.helper(values, idx+1)
            for res_ in result:
                output.append([digit] + res_)
        return output

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        chars = string.ascii_lowercase
        chars_dict = {}
        start = 0
        for idx in range(2, 10):
            increment = 4 if idx == 7 or idx == 9 else 3
            chars_dict[idx] = [val for val in chars[start:start+increment]]
            start += increment
        values = [chars_dict[int(digit)] for digit in digits]
        output = self.helper(values, 0)
        return ["".join(val) for val in output]