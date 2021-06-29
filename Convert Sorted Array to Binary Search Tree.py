### https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-35-bst-3-b1f225f39aa3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    def __init__(self):
        self.root=None
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        for n in nums:
            if self.root==None:
                self.root=TreeNode(n)
            else:
                parent=self.root
                current=self.root                
                while True:
                    if n < current.val:
                        if current.left==None:                            
                            current.left=TreeNode(n)
                            print(current, n)
                            break
                        else:
                            current=current.left
                    elif n > current.val:
                        if current.right==None:
                            current.right=TreeNode(n)
                            print(current, n)
                            break
                        else:
                            current=current.right
        return self.root
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        return self.getNode(nums, 0, len(nums) - 1)
    
    def getNode(self, nums: List[int], l: int, r: int) -> TreeNode:
        if l > r: 
            return None        
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.getNode(nums, l, mid - 1)
        root.right = self.getNode(nums, mid + 1, r)        
        return root
