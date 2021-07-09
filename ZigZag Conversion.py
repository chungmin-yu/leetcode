class Solution:
    def convert(self, s: str, numRows: int) -> str:
        loop=numRows*2-2
        length=len(s)
        if numRows==1:
            return s
        
        ans=''
        #head
        for j in range(0,length,loop):
                ans+=s[j]
        #middle
        for i in range(1,numRows-1):
            #(6-1)-2*0-1=4
            #(6-1)-2*1-1=2
            k=(loop-1)-2*(i-1)-1
            for j in range(i,length,loop):
                ans+=s[j]
                if j+k<length:
                    ans+=s[j+k]
        #tail
        for j in range(numRows-1,length,loop):
                ans+=s[j]
                
        return ans
