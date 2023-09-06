# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        new_array = [None for _ in range(arr_len)]
        i = 0
        j = arr_len - 1
        current_idx = arr_len - 1
        while current_idx >= 0:
            if abs(nums[i]) > abs(nums[j]):
                new_array[current_idx] = nums[i] ** 2
                i += 1
            else:
                new_array[current_idx] = nums[j] ** 2
                j -= 1
            current_idx -= 1
        return new_array