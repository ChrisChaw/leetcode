class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False for _ in range(len(nums))]
        self.dfs(nums, path, res, used)
        return res

    def dfs(self, nums, path, res, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(0, len(nums)):
            # 剪枝 判断重复使用的数字
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                self.dfs(nums, path, res, used)
                # 回溯过程中 将当前的节点从path中删除
                path.remove(path[len(path) - 1])
                used[i] = False
