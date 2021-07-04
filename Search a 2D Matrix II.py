class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for li in matrix:
            for i in li:
                if i==target:
                    return True
        return False
