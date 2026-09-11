# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def traversal(node):
            nonlocal max_sum
            if node is None:
                return 0
            
            left_sum=traversal(node.left)
            if left_sum < 0:
                left_sum = 0
            right_sum=traversal(node.right)
            if right_sum < 0:
                right_sum = 0

            max_sum = max(max_sum , node.val + left_sum + right_sum)
            return node.val + max(left_sum,right_sum)

        traversal(root)
        return max_sum
        
