class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" :
            return 0
        if len(s) == 1:
            return 1

        l, r = 0,1
        res = 0
        t = s[l]
        while r< len(s):
            if s[r] not in t:
                t += s[r]
                r += 1
                res = max(res, len(t))

            else:
                
                l += 1
                t = t[1:]
        return res