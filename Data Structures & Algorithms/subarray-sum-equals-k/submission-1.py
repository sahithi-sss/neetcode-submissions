class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = []
        sm = 0
        for n in nums:
            sm += n
            pref_sum.append(sm)
        res = 0
        #p[j] - p[i-1] = sum(nums[i:j])
        freq = defaultdict(int) # hashmap mapping 
        freq[0] = 1 # so that the window which starts from nums[0] 
        for j in range(len(nums)):
            diff = pref_sum[j] -k #= pref_sum[i-1]
            if diff in freq :
                res += freq[diff] 
            # freq[diff] += 1 -> That means you're storing: “required prefix sums”
            #But we actually need: “prefix sums we have already seen
            freq[pref_sum[j]] += 1
        return res