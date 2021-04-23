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
                if nums[j] < nums[i]:  # 前面的数nums[j]<后面的数nums[i] 状态转移方程:dp[i] = max(dp[i], dp[j] + 1)
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(length):
            res = max(dp[i], res)
        return res


class Solution:
    """
    时间复杂度：O(NlogN)
    空间复杂度：O(N) 最长递增子序列 可以不连续
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp + 二分查找 时间复杂度: O(NlogN)
        tail = [nums[0]]  # 保存其中一个最长上升子序列
        res = 1  # 最终返回的长度
        for num in nums[1:]:
            if num > tail[-1]:
                tail.append(num)
                res += 1
            else:
                # 二分查找tail中第一个比num大的数 并替换为num
                i, j = 0, res
                while i < j:
                    mid = i + (j - i) // 2  # 防止i,j过大 计算溢出
                    if tail[mid] > num:
                        i = mid + 1
                    else:
                        j = mid
                tail[i] = num  # i和j交汇了
        print(tail)
        return res
