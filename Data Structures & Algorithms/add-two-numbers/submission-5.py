# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val
            sm = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) //10

            curr.next = ListNode(sm)
            curr = curr.next
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        return dummy.next