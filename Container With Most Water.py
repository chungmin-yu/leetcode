class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        left=0
        right=len(height)-1
        
        while left<right:
            rect=min(height[left], height[right])*(right-left)
            if rect>area:
                area=rect
            
            if height[left]<height[right]:
                left+=1
            elif height[right]<height[left]:
                right-=1
            elif height[left]==height[right]:
                left+=1
                right-=1
                
        return area 
