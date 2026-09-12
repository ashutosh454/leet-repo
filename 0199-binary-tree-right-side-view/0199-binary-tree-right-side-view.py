# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def reversePostOrder(node,level,ans):
            if node is None:
                return

            if len(ans)==level:
                ans.append(node.val)

            if node.right:
                reversePostOrder(node.right,level+1,ans)

            if node.left:
                reversePostOrder(node.left,level+1,ans)

        ans = []
        reversePostOrder(root,0,ans)
        return ans
            
