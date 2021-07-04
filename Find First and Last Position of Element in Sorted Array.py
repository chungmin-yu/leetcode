class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=-1
        end=-1
        find=False
        for i in range(len(nums)):
            if not find and nums[i]==target:
                start=i
                find=True
            if find and nums[i]!=target:
                end=i-1
                break
                
        #when the target at last element
        if find and end==-1:
            end=len(nums)-1
        return [start,end]
