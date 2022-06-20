# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def helper(self, root, lst):
            if root != None:
                lst.append(root.val)
                helper(self, root.left, lst)
                helper(self, root.right, lst)
                
        helper(self, root, lst)
        return lst
