class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 ; buy = prices[0]
        for p in prices:
            buy = min(p,buy)
            best = max(best, p-buy)
        return best
