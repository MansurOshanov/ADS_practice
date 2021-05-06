class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float(inf)
        max_profit = 0
        for i,v in enumerate(prices):
            if v < min_price:
                min_price = v
            elif v - min_price > max_profit:
                max_profit = v - min_price
        return max_profit