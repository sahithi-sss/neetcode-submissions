class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lst = sorted(list(set(nums)))
        max_len = 1
        cnt = 1
        for i in range(len(lst)-1):
            if lst[i+1] == (lst[i]+1):
                cnt += 1
            else:
                max_len = max(max_len,cnt)
                cnt = 1
        return max(max_len, cnt)