class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:       
        '''
        ans=[]
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    del nums2[j]
                    break
                if nums1[i]<nums2[j]:
                    break
        '''
        
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    del nums2[j]
                    break
        
        return ans
