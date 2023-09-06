# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        current_max = nums[0]

        for num in nums[1:]:
            if current_sum + num > num:
                current_sum += num
            else:
                current_sum = num
            current_max = max(current_max, current_sum)
        return current_max