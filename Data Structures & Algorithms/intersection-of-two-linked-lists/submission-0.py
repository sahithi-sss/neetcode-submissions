# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #a, b = headA, headB
        while headA:
            b = headB
            while b:
                if headA == b :
                    return headA
                b = b.next 
            headA = headA.next

        return 