class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = 0
        a = 0
        b = 0
        
        for i in range(len(nums)):
            if (flag == 0) :
                for j in range(len(nums)) :
                    
                        if (nums[i] + nums[j] == target) and (i!=j):
                            flag = 1
                            a = i
                            b = j
                        else :
                            continue
            else :
                break
        output = [a,b]
        return(output)

                    
