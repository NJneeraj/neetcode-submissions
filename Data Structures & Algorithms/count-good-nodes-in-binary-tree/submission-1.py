# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        d = collections.deque([(root,root.val)])

        while d:
            node, path_max = d.popleft()
            if node.val >= path_max:
                res +=1
            new_max = max(node.val , path_max)
            if node.left:
                d.append((node.left,new_max))
            if node.right:
                d.append((node.right,new_max))
        return res
