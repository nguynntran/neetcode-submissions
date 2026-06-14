# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hash map for checking index
        hash_dict = {}
        for i in range(len(inorder)):
            hash_dict[inorder[i]] = i
        self.pre_idx = 0
        def build(l,r):
            if l > r:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            mid = hash_dict[root_val]
            root = TreeNode(root_val)
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(preorder) - 1)