# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        point = first = ListNode(0)
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        for x in sorted(nums):
            point.next=ListNode(x)
            point=point.next
        return first.next
