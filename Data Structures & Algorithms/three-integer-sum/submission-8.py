class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue #ensures no duplicates in a
            l,r = i+1, len(nums) -1
            while l<r :
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s>0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1 
                    while l<r and nums[l] == nums[l-1]:
                        l+=1 #ensures no dups in l
                        #if else part ensures no dups in r anyways 
                        #(bcz the sum wont match otherwise)
        return res