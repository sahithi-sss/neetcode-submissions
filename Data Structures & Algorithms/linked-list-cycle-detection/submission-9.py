# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0, head)
        s, f = dummy,head
        while f:
            if s== f :
                return True
            s = s.next
            if f.next:
                f = f.next.next
            else:
                return False
        return False            