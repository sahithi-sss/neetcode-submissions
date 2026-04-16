class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        #freq[num in nums] = frequency of num
        count = defaultdict(list)
        for n,f in freq.items():
            #n = num, f = corresponding freq
            count[f].append(n)
        # count[num's freq = x] = list[all those numbers who have freq = x]
        #now we want the last k numbers of count's values
        #BUT! the keys are not necessarily sorted ,ex - {2:[3], 1:[0,5]}
        res = []
        for f in sorted(count.keys(), reverse = True):
            #now f is the freq - highest to lowest
            #now we need to traverse thru the list stored at freq f , in count
            for num in count[f]:
                if len(res)<k:
                    res.append(num)
                #else:
                    #return res
        return res