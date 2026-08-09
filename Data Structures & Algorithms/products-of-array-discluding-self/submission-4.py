class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #identify total number of 0s
        num_zeroes = 0
        for n in nums:
            if n == 0:
                num_zeroes += 1

        if num_zeroes >= 2:
            return [0] * len(nums)
        
        if num_zeroes == 1:
            zero_ind = nums.index(0)
            #find total prod excluding 0
            tot_prod = 1
            for n in nums:
                if n!= 0:
                    tot_prod *= n
            
            res = []
            for n in nums:
                if n != 0:
                    res.append(0)
                else:
                    res.append(tot_prod)

            return res

        #num_zeroes == 0
        tot_prod = 1
        for n in nums:
            if n!= 0:
                tot_prod *= n
        res = []
        for i,n in enumerate(nums):
            res.append(int(tot_prod / n))
        return res