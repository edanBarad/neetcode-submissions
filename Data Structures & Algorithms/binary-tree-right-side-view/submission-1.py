# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            q = [[root]]
            while q:
                nxt_level = []
                for i in range(len(q[-1])):
                    curr = q[-1][i]
                    if curr.right: nxt_level.append(curr.right)
                    if curr.left: nxt_level.append(curr.left)
                ans.append(q[-1][0].val)
                q.pop()
                if nxt_level: q.append(nxt_level)
        return ans