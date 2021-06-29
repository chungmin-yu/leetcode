# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        while l1:
            #add every value of l1
            self.nodes.append(l1.val)
            l1 = l1.next
        while l2:
            #add every value of l2
            self.nodes.append(l2.val)
            l2 = l2.next
        for x in sorted(self.nodes):
            #after sort, construct link-list
            point.next = ListNode(x)
            point = point.next
        #no return first 0
        return head.next
