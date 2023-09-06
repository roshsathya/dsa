# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def match_subtree(self, rootA, rootB):
        if rootA is None and rootB is None:
            return True
        if rootA is None or rootB is None:
            return False
        if rootA.val != rootB.val:
            return False
        left = self.match_subtree(rootA.left, rootB.left)
        if not left:
            return False
        return self.match_subtree(rootA.right, rootB.right)

    def helper(self, root, subroot):
        if root is None:
            return False
        output = False
        if root.val == subroot.val:
            output = self.match_subtree(root, subroot)
            print(root.val, subroot.val, output)
        if output:
            return True
        left = self.helper(root.left, subroot)
        if left:
            return True
        return self.helper(root.right, subroot)
            
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot)