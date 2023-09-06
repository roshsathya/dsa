# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        new_head = head

        prev = None
        while new_head:
            values.append(new_head.val)
            next_head = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next_head

        current_idx = 0
        new_head = prev
        prev = None

        while new_head:
            if values[current_idx] != new_head.val:
                return False    
            next_head = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next_head
            current_idx += 1

        return True