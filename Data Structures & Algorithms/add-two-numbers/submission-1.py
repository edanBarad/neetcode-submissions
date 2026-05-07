# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 =  [], []
        while l1:
            s1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            s2.append(str(l2.val))
            l2 = l2.next

        s1 = int("".join(s1)[::-1])
        s2 = int("".join(s2)[::-1])

        result = s1+s2

        head = ListNode(0)
        curr = head
        while result:
            curr.next = ListNode(result % 10)
            curr = curr.next
            result //= 10
            
        return head.next if head.next else ListNode(0)