class Solution:
    def myAtoi(self, s: str) -> int:
        upperbound=2**31-1
        lowerbound=-(2**31)        
        negative=False
        first=True
        ans=0
        for i in range(len(s)):  
            if first and s[i]==' ':
                pass
            elif first and s[i]=='+':
                first=False
            elif first and s[i]=='-':
                first=False
                negative=True
            elif s[i]!='0' and s[i]!='1' and s[i]!='1' and s[i]!='2' and s[i]!='3' and s[i]!='4' and s[i]!='5' and s[i]!='6' and s[i]!='7' and s[i]!='8' and s[i]!='9':
                if first:
                    return 0
                else:
                    if negative:
                        ans=-ans
                    if ans<lowerbound:
                        ans=lowerbound
                    elif ans>upperbound:
                        ans=upperbound
                    return ans
            else:
                first=False
                ans=ans*10+int(s[i])
        if negative:
            ans=-ans
        if ans<lowerbound:
            ans=lowerbound
        elif ans>upperbound:
            ans=upperbound
        return ans
