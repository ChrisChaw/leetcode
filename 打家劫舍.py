class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        a = [[0 for i in range(2)] for j in range(n)]
        a[0][0] = 0  # 0号房子不偷
        a[0][1] = nums[0]  # 0号房子偷
        if n >= 1:
            for i in range(1, n):
                a[i][0] = max(a[i - 1][0], a[i - 1][1])  # 第i号不偷 第i-1偷或不偷
                a[i][1] = a[i - 1][0] + nums[i]  # 第i号偷 第i-1不偷
        return max(a[n - 1][0], a[n - 1][1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: 1,...,i号房子能偷到的最大价值 偷或不偷
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]


# 化简版的版本
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, now = 0, 0
        for j in nums:
            pre, now = now, max(now, pre + j)  # dp[i] = max(dp[i-1], dp[i-2]+nums[i]) dp[i-1]:now pre:dp[i-2] j:nums[i]
        return now
