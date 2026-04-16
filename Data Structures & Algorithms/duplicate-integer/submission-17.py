class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i , n in enumerate(nums):
            if n in s:
                return True
            else:
                s.add(n)
        return False