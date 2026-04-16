class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if not s :
            return False
        for c in s:
            if c in "({[":
                st.append(c)
            elif c == ")":
                if not st or st[-1] != "(":
                    return False
                else:
                    st.pop()
            elif c == "]":
                if not st or st[-1] != "[":
                    return False
                else:
                    st.pop()
            else :
                if not st or st[-1] != "{":
                    return False
                else:
                    st.pop()
        if st == []:
            return True
        else:
            return False