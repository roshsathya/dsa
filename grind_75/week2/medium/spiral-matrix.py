# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited_set = set()
        current_dir = "right"
        total_elements = len(matrix) * len(matrix[0])
        x,y = 0, 0
        output = []
        while total_elements:
            output.append(matrix[x][y])
            visited_set.add((x,y))
            total_elements -= 1

            if current_dir == 'right':
                if (y+1 >= len(matrix[x]) or (x,y+1) in visited_set):
                    current_dir = "down"
                    x += 1
                else:
                    y += 1
            elif current_dir == 'down':
                if (x+1 >= len(matrix) or (x+1,y) in visited_set):
                    current_dir = "left"
                    y -= 1
                else:
                    x += 1
            elif current_dir == 'left':
                if (y-1 < 0 or (x,y-1) in visited_set):
                    current_dir = "up"
                    x -= 1
                else:
                    y -= 1
            elif current_dir == 'up':
                if (x-1 < 0 or (x-1,y) in visited_set):
                    current_dir = "right"
                    y += 1
                else:
                    x -= 1
        return output

