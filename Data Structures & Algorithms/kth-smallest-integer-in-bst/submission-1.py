# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        result = None
        def inorder(node):
            nonlocal result,cnt
            if not node or result is not None:
               return
            inorder(node.left)
            cnt += 1
            if cnt == k:
              result = node.val
              return 
            inorder(node.right)
        inorder(root)
        return result

