import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #using only pointer, and remeber the best possible ans until then
        min_price = math.inf
        max_profit = 0

        for price in prices:
            min_price = min( min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit        