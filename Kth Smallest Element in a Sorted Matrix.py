class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ma=[]
        for li in matrix:
            for i in li:
                ma.append(i)
        #print(ma)
        ma.sort()
        return ma[k-1]
