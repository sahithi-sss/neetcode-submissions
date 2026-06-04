class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1
        max_freq = max(count.values())
        """
        num_max = 0
        for k in count.keys():
            if count[k] == max_freq:
                num_max += 1
        """
        num_max = sum(freq == max_freq for freq in count.values())
        a = ((max_freq - 1)* n) + max_freq + num_max - 1
        b = len(tasks)
        return max(a,b)
