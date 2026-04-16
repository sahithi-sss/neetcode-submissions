class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((j != i) and (nums[j] == nums[i])):
                    flag = 1
                    break
                
        if (flag == 1):
            output = True
        else :
            output = False

        return output
        