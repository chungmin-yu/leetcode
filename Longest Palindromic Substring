class Solution:
    def longestPalindrome(self, s):
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            #odd palindrome
            self.expandFromCenter(s,i,i)
            #even palindrome
            self.expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxlen]


    def expandFromCenter(self,s,l,r):
        while l > -1 and r < len(s) and s[l] ==s[r]:
            l -= 1
            r += 1

        #(r-l+1)-2:not include head and tail    
        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l + 1
