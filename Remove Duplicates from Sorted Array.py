class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]
        #count from the end to the front
        for i in range(len(nums)-1,-1,-1):
            print(i)
            if nums[i] not in ans:
                ans.append(nums[i])  
            else:
                del nums[i]
