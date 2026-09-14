# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:idx for idx,val in enumerate(inorder)}
        preorder_idx = 0
        def build(inorder_left, inorder_right):
            nonlocal preorder_idx
            if inorder_left > inorder_right:
                return None
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1
            mid = idx_map[root_val]
            root.left = build(inorder_left,mid-1)
            root.right = build(mid + 1, inorder_right)
            return root
        return build(0,len(inorder)-1)

