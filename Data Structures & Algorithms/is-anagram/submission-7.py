class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,s2 = sorted(s), sorted(t)
        if s1 == s2:
            return True
        else:
            return False