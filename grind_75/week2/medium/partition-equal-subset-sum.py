# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:

    def helper(self, nums, curr_sum, idx, memo):
        if curr_sum == 0:
            return True
        if (curr_sum,idx) in memo:
            return memo[(curr_sum, idx)]
        if idx >= len(nums):
            return False
        memo[(curr_sum, idx)] = self.helper(nums, curr_sum-nums[idx], idx+1, memo) or self.helper(nums, curr_sum, idx+1, memo)
        return memo[(curr_sum, idx)]
        

    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total_sum = sum(nums)
        print(total_sum)
        if total_sum % 2 == 1:
            return False
        return self.helper(nums, int(total_sum/2),  0, memo)