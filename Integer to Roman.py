class Solution:
    def intToRoman(self, num: int) -> str:
        #roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans=''
        if num>=1000:
            M=num//1000
            ans+=('M'*M)
            num=num%1000
        if num>=100:
            C=num//100
            num=num%100
            if C==4:
                ans+='C'
                ans+='D'
            elif C==9:
                ans+='C'
                ans+='M'
            elif C>=5:
                ans+='D'
                ans+=( 'C'*(C-5) )
            else:
                ans+=('C'*C)
        if num>=10:
            X=num//10
            num=num%10
            if X==4:
                ans+='X'
                ans+='L'
            elif X==9:
                ans+='X'
                ans+='C'
            elif X>=5:
                ans+='L'
                ans+=( 'X'*(X-5) )
            else:
                ans+=('X'*X)
        if num>=1:
            I=num
            if I==4:
                ans+='I'
                ans+='V'
            elif I==9:
                ans+='I'
                ans+='X'
            elif I>=5:
                ans+='V'
                ans+=( 'I'*(I-5) )
            else:
                ans+=('I'*I)
                
        return ans
