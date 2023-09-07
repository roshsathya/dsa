# https://leetcode.com/problems/coin-change/submissions/

class Solution:

    def helper(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return None
        if amount in memo:
            return memo[amount]
        min_coins = float("inf")
        for coin in coins:
            output = self.helper(coins, amount-coin, memo)
            if output is not None:
                min_coins = min(min_coins, output+1)
        memo[amount] = min_coins
        return min_coins

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        output = self.helper(coins, amount, memo)
        if output == float("inf"):
            return -1
        return output