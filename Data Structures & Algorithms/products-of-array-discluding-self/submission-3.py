class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        zeroes = 0
        for n in nums:
            if n == 0:
                zeroes += 1
            else:
                tot *= n
        if zeroes > 1:
            return [0] * len(nums)
        
        if zeroes == 0:
            res = []
            for n in nums:
                res.append(int(tot/n))
            return res
        
        res = []
        for n in nums:
            if n == 0:
                res.append(tot)
            else:
                res.append(0)
        return res