# https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (0,-1), (-1,0), (1, 0)]
        output = [[None for j in range(len(mat[i]))] for i in range(len(mat))]
        queue = deque()
        visited_set = set()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append(((i,j), 0))
                    visited_set.add((i,j))
                    output[i][j] = 0
                    
        while True:
            try:
                location, distance = queue.popleft()
            except:
                break
            loc_x, loc_y = location
            

            for dir_x, dir_y in directions:
                if dir_x + loc_x < 0 or dir_x + loc_x >= len(mat) or dir_y + loc_y < 0 or dir_y + loc_y >= len(mat[loc_x]):
                    continue
                if (dir_x + loc_x, dir_y + loc_y) in visited_set:
                    continue
                queue.append(((dir_x + loc_x, dir_y + loc_y), distance + 1))
                visited_set.add((dir_x + loc_x, dir_y + loc_y))
                output[dir_x + loc_x][dir_y + loc_y] = distance + 1

        return output