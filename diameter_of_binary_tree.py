# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]
        def dfs(root):
            if root is None:
                return -1
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            height = max(left_height, right_height) + 1
            diameter[0] = max(diameter[0], 2 + left_height + right_height)
            return height
            
        dfs(root)
        return diameter[0]
            