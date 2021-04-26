import sys


# 连续的子序列
def max_sub_array(arr):
    max_so_far = -sys.maxsize  # 相当于s[i]
    max_current = 0  # 相当于s[i-1]
    for i in range(0, len(arr)):
        if max_current + arr[i] >= arr[i]:
            max_current = max_current + arr[i]
        else:
            max_current = arr[i]
        if max_so_far < max_current:
            max_so_far = max_current
    return max_so_far


def maxSubArray(nums):
    # 最大子序和 = 当前元素自身最大 或者 包含之前后最大
    # dp[i] = max(nums[i], nums[i]+dp[i-1])
    dp = nums
    for i in range(1, len(nums)):
        # nums[i-1]代表dp[i-1]
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)
