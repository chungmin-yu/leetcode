# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        temp, length = self.lengthOfTree(root)
        return length
    def lengthOfTree(self, current: TreeNode):
        if current==None:
            return 0,0
        l, ltotal=self.lengthOfTree(current.left)
        r, rtotal=self.lengthOfTree(current.right)
        return max(l,r)+1, max(l+r,ltotal, rtotal)
