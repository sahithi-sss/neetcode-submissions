class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        l,r = 0,0
        res = float('-inf')
        for l in range(0, len(nums)) :
            add = 0
            for r in range(l,len(nums)):
                add += nums[r]
                res = max(add, res)
        return res