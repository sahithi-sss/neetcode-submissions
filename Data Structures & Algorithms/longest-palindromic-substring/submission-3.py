class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n== 1:
            return s
        res = []
        for i in range(len(s)):
            for j in range(1,len(s)):
                l,r = i,j
                while l < r and s[l] == s[r]:
                    l+= 1
                    r-=1
                if l>=r :
                    res.append(s[i:j+1])
        if len(res) >= 1:
            max_len =  max(len(r) for r in res)

        for r in res:
            if len(r) == max_len:
                ans = r
                break
        return r
