# https://leetcode.com/problems/clone-graph/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def helper(self, node, node_dict):
        new_node = Node(node.val)
        node_dict[node] = new_node
        for neighbor in node.neighbors:
            if neighbor in node_dict:
                new_node.neighbors.append(node_dict[neighbor])
            else:
                new_node.neighbors.append(self.helper(neighbor, node_dict))
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        node_dict = {}
        self.helper(node, node_dict)
        return node_dict.get(node)
            
            