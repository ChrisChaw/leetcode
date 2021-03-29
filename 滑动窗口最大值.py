class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if not nums:
            return []
        if k > len(nums):
            return [max(nums)]
        n = len(nums) - k + 1  # n: 滑动窗口的个数
        ans = []
        for i in range(n):
            silidingWin = nums[i:i + k]  # 滑动窗口的区域
            ans.append(max(silidingWin))
        return ans
