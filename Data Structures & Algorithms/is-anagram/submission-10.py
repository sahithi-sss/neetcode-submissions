class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        chart = [0] * 26

        for c in s:
            chars[ord(c)-ord("a")] += 1
        for c in t :
            chart[ord(c) - ord("a")] += 1
        if chars == chart :
            return True
        else:
            return False