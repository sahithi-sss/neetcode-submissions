# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 , num2 = 0,0
        i,j = 0,0
        while l1:
            num1 += int(l1.val) * (10**i)
            i += 1
            l1 = l1.next
        while l2:
            num2 += int(l2.val) * (10 ** j)
            j += 1
            l2 = l2.next

        s = str(num1 + num2)
        s = s[::-1]
        res = ListNode()
        curr = res
        for k in range(len(s)):
            curr.val = int(s[k])
            if k != len(s) -1 :
                curr.next = ListNode() 
                curr = curr.next
        return res