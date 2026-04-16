class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True #base case

        for i in range(n-2, -1,-1):
            # i -> position
            for j in range(0,nums[i]+1):
                if i+j < n and dp[i+j]:
                    dp[i] = True
                    break 
        return dp[0]