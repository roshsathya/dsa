# https://leetcode.com/problems/combination-sum/

class Solution:

    def helper(self, candidates, target, start_idx):
        if target == 0:
            return [[]]
        output = []
        for idx, num in enumerate(candidates):
            if idx < start_idx or num > target:
                continue
            result = self.helper(candidates, target-num, idx)
            for data in result:
                data += [num]
                output.append(data)
        return output

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates, target, 0)