# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        prev= None
        carry = 0
        while curr or l2:
            if curr:
                x = curr.val
            else :
                x = 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            if curr:
                curr.val = total % 10
            else:
                prev.next = ListNode(total % 10)
                curr = prev.next
            prev = curr
            curr = curr.next if curr else None
            l2 = l2.next if l2 else None
        if carry:
            prev.next = ListNode(carry)
        return l1
