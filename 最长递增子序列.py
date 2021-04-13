class Solution:
    """
    时间复杂度：O(N^2)
    空间复杂度：O(N) 最长递增子序列 可以不连续
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        dp = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(length):
            res = max(dp[i], res)
        return res
