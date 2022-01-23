# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        
        def findPaths(root, targetSum, current_list):
            
            if not root:
                return
            
            current_list = current_list.copy()
            current_list.append(root.val)
            if root.left is None and root.right is None and root.val == targetSum:
                result.append(current_list)
                return
            
            
            findPaths(root.left, targetSum-root.val, current_list)
            findPaths(root.right, targetSum-root.val, current_list)
            
        findPaths(root, targetSum, [])
        return result