# https://leetcode.com/problems/number-of-islands/submissions/

class UnionFind:
    def __init__(self, count):
        self.count = count
        self.roots = [i for i in range(count)]

    def find(self, x):
        if self.roots[x] == x:
            return x
        return self.find(self.roots[x])

    def pair(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        print(x,y, root_x, root_y)
        if root_x == root_y:
            return
        if root_x < root_y:
            self.roots[root_y] = root_x
        else:
            self.roots[root_x] = root_y
        self.count -= 1


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        new_grid = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                new_grid[(i,j)] = count
                count += 1
        
        uf = UnionFind(count)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                if new_grid.get((i-1, j)) is not None:
                    uf.pair(new_grid[(i-1, j)], new_grid[(i,j)])
                if new_grid.get((i, j-1)) is not None:
                    uf.pair(new_grid[(i, j-1)], new_grid[(i,j)])
                     
        return uf.count