# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # #HashSet approach
    # def hasCycle(self, head: ListNode) -> bool:
    #     nodes_seen = set()
    #     while head is not None:
    #         if head in nodes_seen:
    #             return True
    #         nodes_seen.add(head)
    #         head = head.next
    #     return False
    
    #Fast and Slow pointer apporach
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    
    
        