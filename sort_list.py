# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        tmp = self.getMiddle(head)
        right = tmp.next
        tmp.next = None    
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        sorted_head = self.merge(left, right)
        
        return sorted_head
    
    def getMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def merge(self, left, right):
        sorted_head = tail = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return sorted_head.next
                
            
            
            
            