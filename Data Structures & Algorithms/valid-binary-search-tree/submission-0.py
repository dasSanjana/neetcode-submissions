# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_val,max_val):
            if not node:
                return True 
            if not (min_val < node.val < max_val):
                return False
            valid_left  = dfs(node.left, min_val,node.val)
            valid_right = dfs(node.right, node.val,max_val)
            return valid_left and valid_right
        return dfs(root,float('-inf'),float('inf'))