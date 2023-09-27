# https://leetcode.com/problems/word-search/

#DFS
class Solution:

    def find_word(self, board, i, j, word, idx, visited_set):
        if idx >= len(word):
            return True
        if(i < 0 or i >= len(board) or j < 0 or j >= len(board[i])):
            return False
        if((i, j) in visited_set):
            return False
        if board[i][j] != word[idx]:
            return False
        visited_set.add((i,j))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for x, y in directions:
            next_i = i + x
            next_j = j + y
            output = self.find_word(board, next_i, next_j, word, idx+1, visited_set)
            if output:
                return True
        visited_set.remove((i,j))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited_set = set()
                    if(self.find_word(board, i, j, word, 0, visited_set)):
                        return True
        return False
        