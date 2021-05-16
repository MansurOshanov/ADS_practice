# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        '''
        BFS traversal
        '''
#         if root is None:
#             if subRoot is None:
#                 return True
#             return False
        
#         queue = collections.deque()
#         queue.append(root)
        
#         while(queue):
#             size = len(queue)
#             for i in range(size):
#                 node = queue.popleft()
#                 if self.isSameTree(node, subRoot):
#                     return True
                
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
                
#         return False

        '''
        DFS traversal
        '''
        if root is None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isSameTree(self, root, subRoot):
        if root is None or subRoot is None:
            return root == subRoot
        
        if root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) \
                and self.isSameTree(root.right, subRoot.right)
        else:
            return False
        
        
        