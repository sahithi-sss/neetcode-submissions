# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            #1- change pointer
            #2 update prev
            #3 update curr
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # by the end of the loop, curr would be at none ( cross the list)
        # and prev would be at the lst point

        return prev