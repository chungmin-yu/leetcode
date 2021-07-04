class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()       
        length=len(nums1)
        #number is odd
        if length%2==1:
            index=(length-1)//2
            return float(nums1[index])
        #number is even
        else:
            index1=length//2
            index2=length//2-1
            return (nums1[index1]+nums1[index2])/2  
