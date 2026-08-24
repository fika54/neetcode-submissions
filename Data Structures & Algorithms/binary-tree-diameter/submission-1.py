# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiam = 0
        def recurse(root):
            nonlocal maxDiam
            if not root:
                return 0
            
            leftHeight = recurse(root.left)
            rightHeight = recurse(root.right)

            diam = leftHeight + rightHeight

            if maxDiam < diam:
                maxDiam = diam

            print(leftHeight, rightHeight)
            
            return 1 + max(leftHeight, rightHeight)

        recurse(root)

        return maxDiam
        