class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s :
            return 
        s_new = ""
        for c in s:
            if c.isalnum():
                s_new += c.lower()
        if s_new == s_new[-1::-1]:
            return True
        else:
            return False