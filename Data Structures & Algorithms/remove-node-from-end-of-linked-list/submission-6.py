# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        while n > 0 and right.next:
            right = right.next
            n = n - 1
        if n != 0: 
            return left.next
        while right.next:
            right = right.next
            left = left.next
        if not left.next:
            return None
        left.next = left.next.next
        return head
