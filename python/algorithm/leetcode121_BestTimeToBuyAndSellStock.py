class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        dp = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            dp[i] = max(prices[i] - min_price, dp[i - 1])
            min_price = min(min_price, prices[i])

        return dp[-1]