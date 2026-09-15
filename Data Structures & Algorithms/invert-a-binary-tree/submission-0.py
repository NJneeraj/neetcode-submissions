# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        left = curr.left
        right = curr.right
        curr.left = self.invertTree(right)
        curr.right = self.invertTree(left)
        return root
