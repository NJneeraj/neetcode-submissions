# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        def inOrder(node):
            if not node:
                return None
            left = inOrder(node.left)
            if left:
                self.arr.append(left.val)
            self.arr.append(node.val)
            right = inOrder(node.right)
            if right:
                self.arr.append(node.right)
        inOrder(root)
        return self.arr[k-1]