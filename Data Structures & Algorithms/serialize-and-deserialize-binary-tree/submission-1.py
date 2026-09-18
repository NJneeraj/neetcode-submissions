# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []

        def preorder(node):
            if not node:
                arr.append("None")
                return
            arr.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(arr)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 1,2,None,None,3,4,None,None,5,None,None ??
        arr = data.split(",")
        i = 0

        def construct():
            nonlocal i
            if arr[i] == "None":
                i += 1
                return None
            node = TreeNode(int(arr[i]))
            i += 1
            node.left = construct()
            node.right = construct()
            return node

        return construct()
