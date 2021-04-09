class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for k, v in dic.items():
            if v > n // 2:
                return k
