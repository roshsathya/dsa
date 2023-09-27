# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, preorder, inorder):
        if not inorder:
            return None
        if self.idx >= len(preorder):
            return None
        node = TreeNode(preorder[self.idx])
        inorder_idx = inorder.index(preorder[self.idx])
        self.idx += 1
        node.left = self.helper(preorder, inorder[:inorder_idx])
        node.right = self.helper(preorder, inorder[inorder_idx+1:])
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        return self.helper(preorder, inorder)