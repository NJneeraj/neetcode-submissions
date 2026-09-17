# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()        
        d.append(root)
        res = []
        if not root:
            return res
        while len(d):
            level = len(d)
            levRes =[]
            for i in range(level):
                curr = d.popleft()
                if curr:
                    levRes.append(curr.val)
                else:
                    continue
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            res.append(levRes)
        return res 