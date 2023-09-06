# https://leetcode.com/problems/longest-common-prefix/

class Solution:

    def find_common_string(self, s, t):
        common_str = []
        idx = 0
        while idx < len(s) and idx < len(t):
            if s[idx] == t[idx]:
                common_str.append(s[idx])
                idx += 1
            else:
                break
        return "".join(common_str)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 1
        first_str = strs[0]
        while idx < len(strs):
            first_str = self.find_common_string(first_str, strs[idx])
            idx += 1
        return first_str