# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        new_head = head
        while new_head:
            next_head = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next_head
        return prev