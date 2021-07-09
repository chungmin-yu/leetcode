class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            number=str(x)
            '''
            number=[]
            while x!=0:
                number.append(x%10)
                x//=10
            '''   
            i=0
            j=len(number)-1
            while True:
                if i>j:
                    return True
                
                if number[i]==number[j]:
                    i+=1
                    j-=1
                else:
                    return False
