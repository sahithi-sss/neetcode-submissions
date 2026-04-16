class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        res = len(nums)
        for i in range( len(nums) ):
            sm = 0
            for j in range(i, len(nums)):
                ln = j - i +1
                sm += nums[j]
                if sm >= target:
                    res = min(ln, res)
                    break
        return res