# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = slow.next
        slow.next = None
        
        
        prev = None
        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp
            
        list1, list2 = head.next, prev
        dummy = head
        while list1 and list2:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
                
            
            
        