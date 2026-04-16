class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) -1
        while l<r :
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        mini = nums[l]

        def binary_search(l,r, target):
            if l > r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(l, mid - 1, target)
            else:
                return binary_search(mid + 1, r, target)

        if nums[l] <= target <= nums[-1]:
            return binary_search(l, len(nums)-1, target)
        else:
            return binary_search(0, l-1, target)