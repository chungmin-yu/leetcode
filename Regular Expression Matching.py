class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        
        #check the first char of s
        if len(s) == 0:
            first_ch_matched = False
        else:
            if p[0] == s[0] or p[0] == '.':                
                first_ch_matched = True
            else:
                first_ch_matched = False
        
        #check second char of p is '*'
        if len(p) >= 2 and p[1] == '*':
            # match zero element -> remove p of two char
            # match one more elment -> remove s of one char
            return self.isMatch(s, p[2:]) or (first_ch_matched and self.isMatch(s[1:], p))
        else:
            # remove the first char and compare the substring
            return first_ch_matched and self.isMatch(s[1:], p[1:])
