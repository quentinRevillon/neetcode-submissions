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

        if root.left:
            inverted_left = self.invertTree(root.left)
        else:
            inverted_left = None

        if root.right:
            inverted_right = self.invertTree(root.right)
        else:
            inverted_right = None

        root.left, root.right = inverted_right, inverted_left
        return root