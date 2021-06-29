class Solution:
    def search(self, nums: List[int], target: int) -> int:
        find = -1
        for i in range(len(nums)):
            if nums[i] == target:
                find=i
                break
        return find  
