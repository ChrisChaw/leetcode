class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心算法 时间复杂度：O(n)
        if nums == []:
            return False
        # endReachable:能跳到最后位置的索引 初始化为最后位置
        endReachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            # 如果第i处位置+最多跳的距离 >= 最后位置处 表示第i处能跳到最后位置
            if nums[i] + i >= endReachable:
                endReachable = i  # 表示第i处能跳到最后位置 endReachable更新为i
        return endReachable == 0  # 第0处索引位置能跳到最后位置
