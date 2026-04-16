from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        l1, l2 = [], []

        que = deque([p])
        while que:
            node = que.popleft()
            if node:
                l1.append(node.val)
                que.append(node.left)
                que.append(node.right)
            else:
                l1.append(None)

        quee = deque([q])
        while quee:
            node = quee.popleft()
            if node:
                l2.append(node.val)
                quee.append(node.left)
                quee.append(node.right)
            else:
                l2.append(None)

        return l1 == l2