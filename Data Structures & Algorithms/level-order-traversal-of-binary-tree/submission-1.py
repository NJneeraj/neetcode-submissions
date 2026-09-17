# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque([root])        
        res = []
        while d:
            level = len(d)
            levRes =[]
            for i in range(level):
                curr = d.popleft()
                levRes.append(curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            res.append(levRes)
        return res 