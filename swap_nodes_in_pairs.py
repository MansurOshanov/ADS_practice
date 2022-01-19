# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # prev -> a -> b -> b.next
        # prev -> b -> a -> b.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next

            prev.next, b.next, a.next = b, a, b.next
            
            prev = a
        
        return dummy.next