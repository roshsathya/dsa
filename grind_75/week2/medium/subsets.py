# https://leetcode.com/problems/subsets/

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         idx = 0
#         output = [[]]
#         while idx < len(nums):
#             new_outputs = []
#             for value in output:
#                 new_outputs.append(value + [nums[idx]])
#             output += new_outputs
#             idx += 1
#         return output

class Solution:

    def helper(self, nums, idx, output):
        if idx >= len(nums):
            return
        new_outputs = []
        for value in output:
            new_outputs.append(value + [nums[idx]])
        output += new_outputs
        self.helper(nums, idx+1, output)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        outputs = [[]]
        self.helper(nums, 0, outputs)
        return outputs
        