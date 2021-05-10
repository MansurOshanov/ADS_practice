# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        queue = collections.deque()
        
        if root is None:
            return result
        
        queue.append(root)
        
        while queue:
            size = len(queue)
            sum = 0
            for i in range(size):
                node = queue.popleft()
                sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(sum/size)
            
        return result
                
        
        