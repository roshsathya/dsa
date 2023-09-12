# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        total_oranges = 0
        visited_set = set()
        rounds = -1
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                total_oranges += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited_set.add((i,j))
                    
        if not total_oranges:
            return 0

        while True:
            current_oranges = len(queue)
            if not current_oranges:
                break
            rounds += 1

            for _ in range(current_oranges):
                current_orange = queue.popleft()
                curr_x, curr_y = current_orange
                total_oranges -= 1

                for x, y in directions:
                    next_x = curr_x + x
                    next_y = curr_y + y
                    if next_x < 0 or next_y < 0 or next_x >= len(grid) or next_y >= len(grid[next_x]):
                        continue
                    if (next_x, next_y) in visited_set or grid[next_x][next_y] == 0:
                        continue
                    queue.append((next_x, next_y))
                    visited_set.add((next_x, next_y))
    
        return rounds if not total_oranges else -1