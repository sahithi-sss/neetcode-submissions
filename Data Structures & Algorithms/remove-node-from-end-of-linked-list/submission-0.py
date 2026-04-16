class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr = head

        while curr:
            cnt += 1
            if curr.next:
                curr = curr.next
            else:
                break

        res = cnt - n + 1

        if res == 1:
            return head.next

        cur = head
        for _ in range(res - 2):
            cur = cur.next

        cur.next = cur.next.next

        return head