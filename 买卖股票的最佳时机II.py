class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                total += prices[i + 1] - prices[i]
        return total


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for j in range(2)] for i in range(len(prices))]  # 定义len(price) * 2 大小的矩阵
        # init
        for i in range(len(prices)):
            dp[i][0] = max((dp[i - 1][0] if i >= 1 else 0),
                           (dp[i - 1][1] if i >= 1 else -float('inf')) + prices[i])  # 第i天买 0:买
            dp[i][1] = max((dp[i - 1][1] if i >= 1 else -float('inf')),
                           (dp[i - 1][0] if i >= 1 else 0) - prices[i])  # 第i天不买 1:不买
        return dp[len(prices) - 1][0]
