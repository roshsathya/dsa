# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, rootA, rootB):
        if rootA is None and rootB is None:
            return True
        if rootA is None or rootB is None:
            return False
        if rootA.val != rootB.val:
            return False
        left = self.helper(rootA.left, rootB.right)
        if not left:
            return False
        return self.helper(rootA.right, rootB.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)