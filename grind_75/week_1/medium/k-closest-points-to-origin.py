# https://leetcode.com/problems/k-closest-points-to-origin/

# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)

        for i in range(k):
            point_x, point_y = points[i]
            distance = point_x**2 + point_y**2
            heappush(heap, (-1*distance, [point_x, point_y]))

        for i in range(k, len(points)):
            point_x, point_y = points[i]
            distance = point_x**2 + point_y**2
            top_dist, top_element = heappop(heap)
            if top_dist*-1 > distance:
                heappush(heap, (-1*distance, [point_x, point_y]))
            else: 
                heappush(heap, (top_dist, top_element))

        output = []
        while k:
            _, top_element = heappop(heap)
            output.append(top_element)
            k -= 1
        
        return output
        