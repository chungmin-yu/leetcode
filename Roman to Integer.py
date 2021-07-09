class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special={'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        ans=0
        prev=None
        for i in range(len(s)):
            if prev==None:                
                ans+=roman[s[i]]
                prev=s[i]
            elif prev+s[i] in special:                
                ans-=roman[prev]
                ans+=special[prev+s[i]]
                prev=s[i]
            else:                
                ans+=roman[s[i]]
                prev=s[i]
        return ans
