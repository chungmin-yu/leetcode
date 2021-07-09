class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0]
        for i in range(1, len(strs)):
            k=0
            while k<len(ans) and k<len(strs[i]): 
                if ans[k]==strs[i][k]:
                    k+=1
                else:
                    break
            ans=ans[:k]
            if k==0:
                return ''
        return ans
