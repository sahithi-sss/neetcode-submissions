class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        longest = ""
        def fnc(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)):
            odd = fnc(i,i)
            even = fnc(i,i + 1)
            if len(odd) > len(longest): longest = odd
            if len(even) > len(longest): longest = even
        return longest