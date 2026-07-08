# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1
        
        if node.left is None:
            return self.minDepth(node.right)+1

        if node.right is None:
            return self.minDepth(node.left)+1

        return min(self.minDepth(node.right) , self.minDepth(node.left)) +1
        
        