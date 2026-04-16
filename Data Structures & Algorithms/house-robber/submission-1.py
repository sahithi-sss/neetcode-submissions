class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            #cache[i] = nums[i] + dfs(i+2)
            #the above wouldnt work bcz you are only considering alternate houses
            #but not the strat where 1,2,1,2 is the possible non robbed houses
            cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return cache[i] 
        return dfs(0)