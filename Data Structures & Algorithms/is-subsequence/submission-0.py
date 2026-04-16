class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0,0
        if len(s) == 0:
            return True
        while p1 <= len(s):
            if p1 == len(s) :
                return True
            if p2 == len(t):
                return False
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else :
                p2 += 1
