# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        while start < end:
            mid = (start + end) // 2
            is_bad_version = isBadVersion(mid)
            if is_bad_version:
                end = mid
            else:
                start = mid + 1
        return start