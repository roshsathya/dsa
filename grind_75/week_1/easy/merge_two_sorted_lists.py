# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        prevHead = None
        list1Head = list1
        list2Head = list2

        while list1Head and list2Head:
            if list1Head.val <= list2Head.val:
                prevHead = list1Head
                list1Head = list1Head.next
                continue

            nextList2Head = list2Head.next
            if prevHead:
                prevHead.next = list2Head
            else:
                list1 = list2Head
            list2Head.next = list1Head

            prevHead = list2Head
            list2Head = nextList2Head

        if list2Head:
            if not prevHead:
                return list2Head
            prevHead.next = list2Head
        
        return list1