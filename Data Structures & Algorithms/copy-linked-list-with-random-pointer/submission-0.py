"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        ans = {None: None}

        curr = head
        while curr:
            ans[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            newNode = ans[curr]
            newNode.next = ans[curr.next]
            newNode.random = ans[curr.random]
            curr = curr.next
    
        return ans[head]