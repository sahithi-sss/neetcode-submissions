# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        # here we have to initiate "0", bcz we want the next to point to head specifically
        left = dummy
        right = head

        while n>0 and right:
            #here by checking "right" we check if it is not null bcz of the update in the prev iteration
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next