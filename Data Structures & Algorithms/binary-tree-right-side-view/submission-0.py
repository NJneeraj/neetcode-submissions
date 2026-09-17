# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        d = deque([root])
        # 
        while d:
            l = len(d)
            curr = None
            for i in range(l):
                curr = d.popleft()
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            res.append(curr.val)
        return res
                
