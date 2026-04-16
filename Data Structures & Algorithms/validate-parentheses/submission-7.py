class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 :
            return False
        stack = [s[0]]
        for i in range(1,len(s)):
            if not stack:
                if s[i] == ")" or s[i] == "]" or s[i] == "}":
                    return False
                else:
                    stack.append(s[i])
            else:
                top = stack[-1]
                if top == "(" and s[i] == ")":
                    stack.pop()
                elif top == "{" and s[i] == "}":
                    stack.pop()
                elif top == "[" and s[i] == "]":
                    stack.pop()
                else:
                    stack.append(s[i])
                
        if len(stack) != 0:
            return False
        else:
            return True