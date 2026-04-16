class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) #number : freq
        count = defaultdict(list) #freq : [number]

        for n in nums:
            if not freq[n]:
                freq[n] = 1
            else:
                freq[n] += 1

        for num, f in freq.items():
            count[f].append(num)

        res  = []
        for f in sorted(count.keys(),reverse = True):
            for num in count[f]:
                if len(res) < k:
                    res.append(num)
        
        return res