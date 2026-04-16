class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in range(len(s)):
            if s[i].isalnum():
                t += s[i].lower()
        for i in range(len(t)):
            j = len(t) - i - 1
            #print(i,j)
            if t[i] != t[j]:
                return False
        return True