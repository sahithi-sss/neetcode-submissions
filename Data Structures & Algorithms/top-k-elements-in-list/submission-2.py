class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #n:freq
        for i in nums:
            count[i] = 1 + count.get(i,0)
        final = [[] for i in range(len(nums)+1)] #stores in buckets
        for n,c in count.items():
            final[c].append(n)
        res = []
        for i in range(len(final)-1, 0, -1):
            for n in final[i]:
                res.append(n)
                if len(res) == k:
                    return res
