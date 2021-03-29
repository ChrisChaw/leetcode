class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left, right = i + 1, n - 1
                while left < right:
                    num_sum = nums[i] + nums[left] + nums[right]
                    if num_sum == 0:
                        s = [nums[i], nums[left], nums[right]]
                        res.append(s)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif num_sum < 0:
                        left += 1
                    else:
                        right -= 1
        return res
