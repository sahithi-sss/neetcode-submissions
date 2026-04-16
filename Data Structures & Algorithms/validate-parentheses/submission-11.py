class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ["(", "{", "["]:
                st.append(c)
            else:
                if c== ")":
                    if st == [] or st[-1] != "(" :
                        return False
                    else:
                        st.pop()
                elif c == "]":

                    if st == [] or st[-1] != "[":
                        return False
                    else:
                        st.pop()
                        
                elif c == "}":
                    if st == [] or st[-1] != "{":
                        return False
                    else:
                        st.pop()
        if not st:
            return True
        else:
            return False