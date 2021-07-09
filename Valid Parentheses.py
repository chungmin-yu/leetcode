class Solution:
    def isValid(self, s: str) -> bool:
        parentheses=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i] =='{' or s[i] == '[':
                parentheses.append(s[i])
            elif s[i]==')':
                if len(parentheses)==0 or parentheses[-1]!='(':
                    return False
                else:
                    del parentheses[-1]
            elif s[i]=='}':
                if len(parentheses)==0 or parentheses[-1]!='{':
                    return False
                else:
                    del parentheses[-1]
            elif s[i]==']':
                if len(parentheses)==0 or parentheses[-1]!='[':
                    return False
                else:
                    del parentheses[-1]
        
        if len(parentheses)==0:
            return True
        else:
            return False
