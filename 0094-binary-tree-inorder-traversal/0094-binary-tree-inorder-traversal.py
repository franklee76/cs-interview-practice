# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)       # Traverse left subtree
            output.append(node.val)  # Visit current node
            inorder(node.right)      # Traverse right subtree
        inorder(root)
        return output

        