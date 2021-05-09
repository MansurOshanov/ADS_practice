# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        '''
        The first idea is to convert LLs into arrays, merge and convert back.
        It would take O(m+n) time and O(m+n) extra space for arrays.
        '''
        
#         arr1 = []
#         arr2 = []
        
#         while l1:
#             arr1.append(l1.val)
#             l1 = l1.next
#         while l2:
#             arr2.append(l2.val)
#             l2 = l2.next
        
#         merged_arr = []
#         i = 0
#         j = 0
#         while i!=len(arr1) and j!=len(arr2):
#             if arr1[i] < arr2[j]:
#                 merged_arr.append(arr1[i])
#                 i += 1
#             else:
#                 merged_arr.append(arr2[j])
#                 j += 1
#         if i == len(arr1):
#             merged_arr.extend(arr2[j:])
#         else:
#             merged_arr.extend(arr1[i:])
        
#         curr_node = ListNode()
#         head = curr_node
#         for i,v in enumerate(merged_arr):
#             new_node = ListNode(v)
#             curr_node.next = new_node
#             curr_node = curr_node.next
            
#         return head.next
    
        '''
        After trying array aproach, it seemed clear that converting 
        to array was unnessesary.
        '''
    
        head = ListNode()
        current_node = head

        while(l1 and l2):
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next

        if l1:
            current_node.next = l1
        else:
            current_node.next = l2

        return head.next
    
            
                
        
        