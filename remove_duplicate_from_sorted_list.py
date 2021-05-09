# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        First idea is to create HashSet and check if element have already appeared
        in Linked List before. O(n) time and O(n) memory though.
        '''
        # curr_node = head
        # prev = head
        # dublicates = set()
        # while curr_node:
        #     if curr_node.val in dublicates:
        #         prev.next = curr_node.next
        #     else:
        #         dublicates.add(curr_node.val)
        #         prev = curr_node
        #     curr_node = curr_node.next
        # return head
        
        '''Now, let's try to solve in O(1) space. Since LL is sorted, dublicate elements
        will be next to each other. So we can always compare current node with previous
        one.
        '''
        # checking edge case when head is None
        curr_node = head.next if head else head
        
        prev = head
        while curr_node:
            if curr_node.val == prev.val:
                prev.next = curr_node.next
            else:
                prev = curr_node
            curr_node = curr_node.next
        return head
        
            
                
        