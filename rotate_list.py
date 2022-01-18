# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        size = 1
        curr = head
        while curr.next:
            curr = curr.next
            size += 1
        tail = curr
        tail.next = head
        
        moves = k % size
        
        for i in range(size - moves):
            head = head.next
            tail = tail.next
        tail.next = None
        
        return head