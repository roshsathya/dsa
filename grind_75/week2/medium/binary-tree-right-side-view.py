# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        output = []
        while True:
            current_len = len(queue)
            if not current_len:
                break
            found_node = False
            for _ in range(current_len):
                current_node = queue.pop()
                if not found_node:
                    output.append(current_node.val)
                    found_node = True
                if current_node.right:
                    queue.appendleft(current_node.right)
                if current_node.left:
                    queue.appendleft(current_node.left)
        return output
            