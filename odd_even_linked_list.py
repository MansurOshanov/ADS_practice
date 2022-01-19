# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        even_start = curr.next
        size = 1
        while curr.next:
            size += 1
            
            pre_last = curr
            last = curr.next
            
            curr.next = curr.next.next
            curr = last
            
        if size%2==0:
            pre_last.next = even_start
        else:
            last.next = even_start
        
        return head