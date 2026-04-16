class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_chars = s.replace(" ","")
        s_chars = s_chars.replace("?","")
        s_chars = s_chars.lower()
        s_chars_new = []
        for char in s_chars :
            if (char.isalnum() == True):
                s_chars_new.append(char)
            else:
                continue
        #print(s_chars)
        #s_char_rev = []
        s_chars_rev = s_chars_new[::-1]
        #print(s_chars_rev)
        """
        for char in s_chars_rev :
            if (char.isalnum() == True):
                s_char_rev.append(char)
            else:
                continue
                """
        if (s_chars_new == s_chars_rev):
            return True
        else :
            return False

