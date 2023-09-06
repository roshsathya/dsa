# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        if left is False:
            return False
        right = self.helper(root.right)
        if right is False:
            return False
        if abs(left - right) > 1:
            return False
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        output = self.helper(root)
        print(output)
        if output is False:
            return False
        return True

    