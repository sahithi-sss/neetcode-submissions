class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = 0
        p = 0
        while p < len(nums):
            if nums[p] == 0:
                nums.pop(p)
                zeroes += 1
            else:
                p += 1
        for z in range(zeroes):
            nums.append(0)