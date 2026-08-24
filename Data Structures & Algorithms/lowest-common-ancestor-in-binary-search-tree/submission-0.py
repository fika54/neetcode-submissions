# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None

        def recurse(root):
            nonlocal lca
            nonlocal p
            nonlocal q

            if not root:
                return 0

            calc = 0

            if root.val == p.val or root.val == q.val:
                calc = 1
            
            calc += recurse(root.left)
            calc += recurse(root.right)

            if calc == 2 and lca == None:
                lca = root
            
            return calc
        recurse(root)
        return lca
            


        