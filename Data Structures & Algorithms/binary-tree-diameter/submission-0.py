# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        if root is None:
            return 0 
        def treeHeight(node):
            if node is None:
                return 0
            left = treeHeight(node.left)
            right = treeHeight(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        treeHeight(root)
        return self.res