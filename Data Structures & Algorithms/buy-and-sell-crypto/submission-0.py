class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i, today in enumerate(prices):
            for future in prices[i + 1:]:
                max_profit = max(max_profit, future - today)

        return max_profit