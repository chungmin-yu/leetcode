# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1=0
        num1=0
        number2=0
        num2=0
        while l1:
            number1=number1+l1.val*(10**num1)
            l1=l1.next
            num1=num1+1
        while l2:
            number2=number2+l2.val*(10**num2)
            l2=l2.next
            num2=num2+1
        ans=number1+number2
        print(number1)
        print(number2)
        print(ans)        
        if ans==0:
            return ListNode(0)
        head=point=ListNode(0)
        while ans!=0:
            point.next=ListNode(ans%10)
            point=point.next
            ans//=10
        return head.next
