class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                res.append("".join(stack))
                return 

            if num_close < num_open:
                stack.append(")")
                backtrack(num_open,num_close+1)
                stack.pop()
            
            if num_open < n:
                stack.append("(")
                backtrack(num_open+1, num_close)
                stack.pop()
            
        backtrack(0,0)
        return res