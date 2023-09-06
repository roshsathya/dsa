# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = float("-inf")
        output = float('-inf')
        idx = len(prices)-1
        while idx >= 0:
            if prices[idx] > current_max:
                current_max = prices[idx]
            else:
                output = max(output, current_max - prices[idx])
            idx -= 1
        if output == float("-inf"):
            return 0
        return output