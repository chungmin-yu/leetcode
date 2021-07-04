# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
           return self.isMirror(root, root)
    
    def isMirror(self, t1, t2) -> bool:        
        # two side is empty at the same time -> true
        if not t1 and not t2:
            return True
        # only one side is empty at the same time -> false
        elif not t1 or not t2:
            return False
        
        #check continue
        return t1.val==t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
