from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a letter:freq map
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1
        for c in t:
            t_map[c] += 1
        
        return True if s_map == t_map else False