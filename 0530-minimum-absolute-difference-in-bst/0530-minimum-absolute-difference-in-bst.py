# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff=float('inf')
        self.prev_node=None

        def in_order(node):
            if not node:
                return

            in_order(node.left)

            if self.prev_node is not None:
                curr_diff= node.val-self.prev_node.val
                self.min_diff=min(self.min_diff,curr_diff)

            self.prev_node=node

            in_order(node.right)

        in_order(root)
        return self.min_diff