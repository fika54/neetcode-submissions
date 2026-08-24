# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxDepth = 0

        def recurse(root: Optional[TreeNode], depth):
            nonlocal maxDepth
            if not root:
                if depth > maxDepth:
                    maxDepth = depth
                return None
            else:
                depth += 1
            
            recurse(root.left, depth)
            recurse(root.right, depth)
            return None
        
        recurse(root, 0)

        return maxDepth
            



        