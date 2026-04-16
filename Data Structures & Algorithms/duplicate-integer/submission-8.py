class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = []
        for i,n in enumerate(nums):
            if n not in s:
                s.append(n)
            else:
                return True
        return False