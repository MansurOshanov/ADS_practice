# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        Basic idea is to run BFS and count depth
        '''
        
#         if root is None:
#             return 0
        
#         queue = collections.deque()
#         queue.append(root)
#         depth = 0
#         while queue:
#             size = len(queue)
#             for i in range(size):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             depth += 1
#         return depth

        '''
        Second idea is to run DFS. More precisely, ask each child node at which
        level they are located, take max and add one.
        '''
        
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
    
    