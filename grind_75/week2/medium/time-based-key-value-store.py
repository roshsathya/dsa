# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values_array = self.keys.get(key)
        if not values_array:
            return ""
        start = 0
        end = len(values_array)-1
        while start < end:
            mid = (start + end) // 2
            if timestamp > values_array[mid][0]:
                start = mid + 1
            else:
                end = mid
        if timestamp < values_array[start][0]:
            if start == 0:
                return ""
            start -= 1
        return values_array[start][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)