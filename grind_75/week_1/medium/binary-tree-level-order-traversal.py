# https://leetcode.com/problems/binary-tree-level-order-traversal/


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        output = []

        while True:
            if not len(queue):
                break
            current_len = len(queue)
            current_level = []
            for _ in range(current_len):
                top_element = queue.popleft()
                current_level.append(top_element.val)
                if top_element.left:
                    queue.append(top_element.left)
                if top_element.right:
                    queue.append(top_element.right)
            output.append(current_level)

        return output