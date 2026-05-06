class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, profit = prices[0], 0
        for p in prices:
            profit = max(profit, p - min_price)
            min_price = min(min_price, p)
        return profit