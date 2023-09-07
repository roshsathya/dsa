# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range(len(nums))]
        right = [1 for i in range(len(nums))]

        idx = 1
        while idx < len(nums):
            left[idx] = nums[idx-1] * left[idx-1]
            idx += 1

        idx = len(nums)-2
        while idx >= 0:
            right[idx] = nums[idx+1] * right[idx+1]
            idx -= 1

        return [left[i]*right[i] for i in range(len(nums))]
