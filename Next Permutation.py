class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        success=False
        for i in range(len(nums)-1, 0 , -1):
            #find first decreasing element
            if nums[i]>nums[i-1]:
                temp=nums[i-1] 
                for j in range(len(nums)-1, i-1 , -1):
                    #find just larger than temp element
                    if nums[j]>temp:
                        nums[i-1]=nums[j]
                        nums[j]=temp
                        break
                #after swapping, reverse the element back of i-1
                nums[i:]=sorted(nums[i:])
                success=True
                break
        #if the largest, reverse to get lowest
        if not success:
            nums.reverse()
