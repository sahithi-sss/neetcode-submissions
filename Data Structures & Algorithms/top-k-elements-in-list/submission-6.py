class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        count = defaultdict(list)
        for n, f in freq.items():
            count[f].append(n)

        res = []
        for f in sorted(count.keys(), reverse = True):
            for num in count[f]:
                if len(res)< k:
                    res.append(num)
        return res