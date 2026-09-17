# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, mn, mx):
            if not node:
                return True
            if not (mn < node.val < mx):
                return False
            is_left_valid = not node.left or isValid(node.left,mn,node.val)
            is_right_valid = not node.right or isValid(node.right,node.val,mx)
            return is_left_valid and is_right_valid  
        
        return isValid(root, float("-infinity"),float("infinity"))