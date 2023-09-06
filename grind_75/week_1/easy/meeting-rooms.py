# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x[0])
        prev_interval = intervals[0]
        for interval in intervals[1:]:
            start, end = interval
            if prev_interval[1] > start:
                return False
            prev_interval = interval
        return True