# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def helper(self, n, memo):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        total = 0
        for step in range(1, 3):
            total += self.climbStairs(n-step)
        memo[n] = total
        return total

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)