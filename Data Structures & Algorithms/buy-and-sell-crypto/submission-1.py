class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L, R = 0, 1
        while (R <= len(prices) - 1):
            if prices[L] >= prices[R]:
                L = R
                R += 1
            else:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
                R += 1
        return max_profit