class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        left=0
        ans=0
        for i in range(len(s)):
            print(window)
            if s[i] not in window:
                window.append(s[i])
            else:
                #delete
                for j in range(len(window)):
                    if s[i]==window[j]:
                        for k in range(j+1):
                            del window[0]
                        left=left+(j+1)
                        break
                window.append(s[i])
            ans=max(ans,i-left+1)
                    
        return ans
