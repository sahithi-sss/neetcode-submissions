from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        # sort keys by frequency (descending)
        sorted_nums = sorted(count, key=lambda x: count[x], reverse=True)
        
        return sorted_nums[:k]
