# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            prev_start_num = None
            prev_end_num = None
            while start < end:
                current_sum = sum([nums[i], nums[start], nums[end]])
                if current_sum == 0: 
                    if nums[start] != prev_start_num or nums[end] != prev_end_num:
                        output.append([nums[i], nums[start], nums[end]])
                    prev_end_num = nums[end]
                    end -= 1
                    prev_start_num = nums[start]
                    start += 1
                elif current_sum > 0:
                    prev_end_num = nums[end]
                    end -= 1
                elif current_sum < 0:    
                    prev_start_num = nums[start]
                    start += 1

        return output