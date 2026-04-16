class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0 #contiguous sum
        for n in nums:
            if curr < 0:
                curr = n
            else:
                curr += n
            res = max(res,curr)
        return res
