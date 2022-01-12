# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # k: start of the loop at kth node
        # n: length of the loop
        # When slow pointer reaches kth node, fast pointer is at 2k node. So fast pointer is k steps ahead. Or if k>n, k mod n steps ahead
        # G = k mod n : how many steps fast pointer ahead
        # n - G: steps so that fast pointer reaches slow pointer.
        # Since slow pointer moved (n-G) steps form start of the loop, it needs to move n-(n-G) = G steps to reach the start of the loop.
        # G = k mod n ====> k = G + n*m where m is any interger
        # k = G
        
        
        fast = slow = head
        
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return fast
        
        
        