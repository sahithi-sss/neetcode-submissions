class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
                # returns True = 1 , when i == n -> only one step needed
                # returns False = 0 , when i != n -> i.e. i > n , hence no more steps needed
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)

            