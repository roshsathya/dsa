class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        sum_dict = {}
        for idx, num in enumerate(nums):
            if target-num not in sum_dict:
                sum_dict[num] = idx
            else:
                output += [sum_dict.get(target-num), idx]
        return output