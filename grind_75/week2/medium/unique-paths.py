# https://leetcode.com/problems/unique-paths/

class Solution:

    def helper(self, curr_m, curr_n, m, n):
        if curr_m == m -1 and curr_n == n-1:
            return 1
        if curr_m >= m or curr_n >= n:
            return 0
        if (curr_m, curr_n) in self.visited_dict:
            return self.visited_dict[(curr_m, curr_n)]
        option1 = self.helper(curr_m+1, curr_n, m, n)
        option2 = self.helper(curr_m, curr_n+1, m, n)
        self.visited_dict[(curr_m, curr_n)] = option1 + option2
        return option1 + option2

    def uniquePaths(self, m: int, n: int) -> int:
        self.visited_dict = {}
        self.total = 0
        return self.helper(0,0,m,n)