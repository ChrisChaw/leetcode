class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        # 不抢第一个 最后一个可抢可不抢
        dp1 = [0 for i in range(n)]
        dp1[0] = 0  # 不抢第一个
        dp1[1] = nums[1]  # 抢第二个
        for i in range(2, n):  # 最后一个 可抢dp1[i - 2] + nums[i] 可不抢dp1[i - 1]
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        # 抢第一个 不抢最后一个
        dp2 = [0 for i in range(n)]
        dp2[0] = nums[0]  # 抢第一个
        dp2[1] = max(nums[0], nums[1])  # 第二个抢或不抢
        for i in range(2, n - 1):  # 不抢最后一个(最后一个索引是n-2处)
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[n - 1], dp2[n - 2])
