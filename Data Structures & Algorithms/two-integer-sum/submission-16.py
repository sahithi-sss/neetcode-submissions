class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {} #complement: index 
        for i, n in enumerate(nums):
            rem = target - n
            if n in complement: # searches in keys by default
                return [complement[n], i]
            complement[rem] = i
        return