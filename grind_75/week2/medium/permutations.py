# https://leetcode.com/problems/permutations/

class Solution:

    def helper(self, nums, used_list):
        if all(used_list):
            return [[]]
        output = []
        for idx, num in enumerate(nums):
            if used_list[idx]:
                continue
            new_list = used_list[:]
            new_list[idx] = True
            result = self.helper(nums, new_list)
            for data in result:
                data = [num] + data
                output.append(data)
        return output

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, [False for _ in range(len(nums))])