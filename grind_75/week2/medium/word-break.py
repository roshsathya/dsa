# https://leetcode.com/problems/word-break/

class Solution:

    def helper(self, s, word_list, memo):
        if s == "":
            return True

        if s in memo:
            return memo[s]
            
        output = False
        for word in word_list:
            idx = s.find(word)
            if idx == -1 or (idx > 0 and idx < len(s)-len(word)):
                continue
            str_list = list(s)
            new_str = "".join(str_list[0:idx] + str_list[idx+len(word):])
            output = self.helper(new_str, word_list, memo)
            if output is True:
                break

        memo[s] = output
        return output
            

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.helper(s, wordDict, memo)