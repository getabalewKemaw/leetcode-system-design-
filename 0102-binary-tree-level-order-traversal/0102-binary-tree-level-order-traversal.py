# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]
        quee=deque([root])
        while quee:
            level_size=len(quee)
            current_level=[]
            for _ in range(level_size):
                node=quee.popleft()
                current_level.append(node.val)
                if node.left:
                    quee.append(node.left)
                if node.right:
                    quee.append(node.right)
            result.append(current_level)
        return result