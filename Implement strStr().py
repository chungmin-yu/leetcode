class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or len(needle)==0:
            return 0
        k=len(needle)
        for i in range(len(haystack)):
            if len(haystack)-i < k :
                break                
            if haystack[i]==needle[0]:
                if haystack[i:i+k]==needle:
                    return i
                
        return -1
