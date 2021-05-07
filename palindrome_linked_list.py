# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         #1 approach: Convert it to list, check if list is palindrome
#         #Takes extra O(n) memory
#         arr = []
        
#         while head:
#             arr.append(head.val)
#             head = head.next
        
#         l, r  = 0, len(arr) - 1
#         while l<=r:
#             if arr[l] != arr[r]:
#                 return False
#             l += 1
#             r -= 1
            
#         return True


    # slow and fast pointer apporach. Takes only O(1) memory
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        #at this stage slow pointer should be at the middle of linked list
        
        prev = None
        while slow:
            forward = slow.next
            slow.next = prev
            prev = slow
            slow = forward
        # now second half of linked list points backwards

        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

    
    
                
        