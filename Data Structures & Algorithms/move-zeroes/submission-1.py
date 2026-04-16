class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p = -1 # tracks the first zero
        for i in range(len(nums)):
            if nums[i] == 0:
                p = i
                break
        if p != -1:
            for t in range(len(nums)):
                if nums[t] != 0 and (p < t):
                    nums[t], nums[p] = nums[p], nums[t]
                    p += 1