# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current_node = head
        check_node = head
        
        while(check_node and check_node.next):
            current_node = current_node.next
            check_node = check_node.next.next
        return current_node