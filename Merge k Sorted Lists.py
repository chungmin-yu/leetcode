# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                #add every value
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            #after sort, construct link-list
            point.next = ListNode(x)
            point = point.next
        #no return first 0
        return head.next
