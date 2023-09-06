# https://leetcode.com/problems/insert-interval/

class Solution:
    def bst(self, intervals, newInterval):
        start = 0
        end = len(intervals) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_interval = intervals[mid]
            if mid_interval[0] > newInterval[0]:
                end = mid - 1
            elif mid_interval[0] < newInterval[0]:
                start = mid + 1
            else:
                if mid_interval[1] < newInterval[1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return start

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_at = self.bst(intervals, newInterval)
        new_list = intervals[0:insert_at]
        if not insert_at:
            new_list = [newInterval]

        for current_interval in [newInterval] + intervals[insert_at:]:
            if current_interval[0] <= new_list[-1][1]:
                new_list[-1][1] = max(current_interval[1], new_list[-1][1])
            else:
                new_list.append(current_interval)
        return new_list