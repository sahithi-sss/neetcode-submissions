class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums :
                x = nums.index( target - nums[i] )
                if x > i:
                    return [i,x]
                elif x< i:
                    return [x,i]