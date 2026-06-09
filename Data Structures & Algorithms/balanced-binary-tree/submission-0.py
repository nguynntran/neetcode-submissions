# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.Balanced = True
        def treeHeight(node):
            if node is None:
                return 0
            left = treeHeight(node.left)
            right = treeHeight(node.right)
            if abs(left - right) > 1:
                self.Balanced = False  
            return 1 + max(left, right)
        
        treeHeight(root)
        return self.Balanced
