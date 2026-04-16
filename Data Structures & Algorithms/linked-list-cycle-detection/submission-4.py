# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast and fast.next:
            # bcz fast moves twice as fast as the slow pointer
            # fast moves 2 points when slow moves 1
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                # this would be inevitable in the case that there exists a loop
        return False