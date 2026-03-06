"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        # if the node does not hv any child only root
        if not root.children:
            return 1
        depths=[self.maxDepth(child) for child in root.children]
        return 1 + max(depths)