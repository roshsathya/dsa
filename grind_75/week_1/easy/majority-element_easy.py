# https://leetcode.com/problems/majority-element/

from heapq import heapify, heappush, heappop

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        heap = []
        heapify(heap)

        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        
        for num, value in nums_dict.items():
            heappush(heap, (-1*value, num))
        
        _ , output = heappop(heap)
        return output