# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []
        
        def helper(root):
            if not root: return
            helper(root.left)
            in_order.append(root.val)
            if len(in_order) == k:
                return in_order[-1]
            helper(root.right)
        
        helper(root)
        return in_order[k-1]