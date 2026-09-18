# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float("-inf")
        def dfs(node,total):
            nonlocal global_max
            if not node:
                return 0
            left_max = max(0,dfs(node.left,total))
            right_max = max(0,dfs(node.right,total))
            curr_max = node.val + left_max + right_max
            if curr_max > global_max:
                global_max = curr_max
            return node.val + max(left_max , right_max)

        dfs(root,0) 
        return global_max