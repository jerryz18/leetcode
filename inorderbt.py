# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
            
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #inorder: left, node, right
        lst = []
        def helper(self, root, lst):
            if root != None:
                helper(self, root.left, lst)
                lst.append(root.val)
                helper(self, root.right, lst)
                
        helper(self, root, lst)
        return lst
        
