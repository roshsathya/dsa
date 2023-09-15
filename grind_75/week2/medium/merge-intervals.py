# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        output = [intervals[0]]
        for idx in range(1, len(intervals)):
            last_interval = output[-1]
            current_interval = intervals[idx]
            if last_interval[1] >= current_interval[0]:
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                output.append(current_interval)
        return output
