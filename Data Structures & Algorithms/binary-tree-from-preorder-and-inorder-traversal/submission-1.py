# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        cache = {}
        for i in range(len(inorder)):
            cache[inorder[i]] = i
        
        def build(pre_start,in_start,in_end):
            nonlocal cache,preorder,inorder
            if in_start > in_end:
                return None
            val = preorder[pre_start]
            root = TreeNode(val)
            
            mid = cache[val]
            root.left = build(pre_start + 1 ,in_start ,mid - 1)
            root.right = build(pre_start + 1 + (mid - in_start), mid + 1,in_end)
            return root    

        return build(0,0,len(inorder) - 1)