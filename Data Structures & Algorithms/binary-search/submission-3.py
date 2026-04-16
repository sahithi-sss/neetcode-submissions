class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r,nums,target):
            if l>r:
                return -1
            mid = (r-l) +1 //2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return binary_search(l,mid-1,nums,target)
            else:
                return binary_search(mid+1, r,nums,target)
        return binary_search(0,len(nums)-1,nums, target)