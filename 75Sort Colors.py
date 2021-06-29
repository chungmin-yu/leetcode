class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=nums.count(0)
        white=nums.count(1)
        blue=nums.count(2)
        nums.clear()
        for i in range(red):
            nums.append(0)
        for i in range(white):
            nums.append(1)
        for i in range(blue):
            nums.append(2)
        """
        Do not return anything, modify nums in-place instead.
        """
        
