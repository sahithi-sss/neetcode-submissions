from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #o/p = list of lists
        #create a dictionary -> key = tuple having the freq of char , value = list of words satisfying having that count map
        res = defaultdict(list)

        for word in strs:
            vec = [0] * 26
            for ch in word:
                vec[ord(ch) - ord("a")] += 1
            res[tuple(vec)].append(word)

        return list(res.values())