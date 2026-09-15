# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (q and not p) or (p and not q):
            return False
        if not p and not q:
            return True
        val = p.val == q.val
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right,q.right)
        return left and right and val