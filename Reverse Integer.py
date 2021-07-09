class Solution:
    def reverse(self, x: int) -> int:
        upperbound=2**31-1
        lowerbound=-(2**31)
        #print(upperbound,lowerbound)
        ans=0
        if x==0:
            ans=0
        elif x>0:
            while x!=0:
                ans=ans*10+x%10
                x//=10
        elif x<0:
            x=-x
            while x!=0:
                ans=ans*10+x%10
                x//=10
            ans=-ans            
            
        if ans<lowerbound or ans>upperbound:
            return 0
        return ans
