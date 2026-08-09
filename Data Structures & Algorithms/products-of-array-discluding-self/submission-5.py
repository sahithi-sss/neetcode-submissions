class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        pref = 1
        for i, n in enumerate(nums):
            res[i] = pref
            pref *= n
        
        #right now the res array stores the left prefixes

        suff = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suff
            suff *= nums[i]

        return res