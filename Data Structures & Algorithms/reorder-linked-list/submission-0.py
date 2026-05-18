# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #First well find the second half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
    
        #Now reverse the second half
        prev, curr = None, second_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        second_head = prev

        #Merge lists
        if slow:
            slow.next = None
            
        first_head = head
        while first_head and second_head:
            tmp1, tmp2 = first_head.next, second_head.next
            
            first_head.next = second_head
            second_head.next = tmp1
            
            first_head, second_head = tmp1, tmp2
            