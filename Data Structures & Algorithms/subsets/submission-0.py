class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset_arr = []
        def dfs(i):
            if i >= len(nums) :
                result.append(subset_arr.copy())
                return
            #left decision
            subset_arr.append(nums[i])
            dfs(i+1)   
            #right decision (skipping)
            subset_arr.pop()
            dfs(i+1)
        dfs(0)
        return result
    
