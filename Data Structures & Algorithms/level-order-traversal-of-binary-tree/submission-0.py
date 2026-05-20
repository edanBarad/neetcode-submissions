# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        q = deque([root])
        while q:
            level_size = len(q)
            current_level = []
            for i in range(level_size):
                current_node = q.popleft()
                current_level.append(current_node.val)
                if current_node.left: q.append(current_node.left)
                if current_node.right: q.append(current_node.right)
            ans.append(current_level)
        return ans