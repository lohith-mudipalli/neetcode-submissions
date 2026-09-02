class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase = prices[0]
        maximum_profit = 0

        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - purchase
            maximum_profit = max(maximum_profit, profit)

            if sell < purchase:
                purchase = sell

        return maximum_profit

        