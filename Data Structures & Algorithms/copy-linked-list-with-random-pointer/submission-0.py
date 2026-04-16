"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head
        res = {}
    
        while temp:
            res[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            if temp.next:
                res[temp].next = res[temp.next]
            if temp.random:
                res[temp].random = res[temp.random]
            temp = temp.next
            
        return res[head]