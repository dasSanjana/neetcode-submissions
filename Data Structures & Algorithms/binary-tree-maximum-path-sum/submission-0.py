# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max_sum = float('-inf') 
        def get_max(node):
            if not node:
                return 0
            left_ans = max(get_max(node.left),0)
            right_ans = max(get_max(node.right),0)
            current_path_sum = node.val + left_ans+ right_ans
            self.global_max_sum = max(self.global_max_sum , current_path_sum)
            return node.val + max(left_ans,right_ans)
        get_max(root)
        return self.global_max_sum

