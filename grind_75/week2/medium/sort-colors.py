# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        k = len(nums)-1

        while j <= k:
            if nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            elif nums[i] == 0:
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            elif nums[j] == 2 or nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]