# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''Simple idea is to reverse each arrow. We will need temp nodes for that'''
        
        prev = None
        curr_node = head
        
        while curr_node:
            next_temp = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_temp
        
        return prev
            
        