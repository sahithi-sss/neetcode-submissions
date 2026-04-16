# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen :
                return True
            seen.add(curr)
            curr = curr.next
        return False
        # here notice that we are not just storring the value
        # at the curr pointer, but the "node" itself
        #thus we avoid issues if there are any duplicates
        # if there were no duplicates , we could have easily stored the seen as a list and not a dictionary