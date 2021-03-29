class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums.extend([0] * n)
