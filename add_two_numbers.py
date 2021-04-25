# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        remainder = 0
        result = ListNode()
        current_node = result
        while p != None or q != None:
            x = p.val if p!= None else 0
            y = q.val if q!= None else 0
            sum_ = x + y + remainder
            remainder = sum_ // 10
            sum_ = sum_ % 10
            
            
            current_node.next = ListNode(sum_)
            current_node = current_node.next
            
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        
        if remainder >= 1:
            current_node.next = ListNode(remainder)
        return result.next
