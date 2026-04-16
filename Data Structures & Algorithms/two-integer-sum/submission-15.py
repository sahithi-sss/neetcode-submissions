class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = defaultdict(int)
        for i,n in enumerate(nums):
            r = target - n
            if r in rem:
                return [rem[r], i]
            rem[n] = i