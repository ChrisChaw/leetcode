class Solution:  # 二分查找 时间复杂度：O(lgn)
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # 当[0, mid]有序时，向后规约条件
            if (nums[0] <= nums[mid] and (nums[mid] < target or nums[0] > target)):
                low = mid + 1
            # 当nums[0]>nums[mid]时 说明[0, mid]发生了旋转，向后规约条件
            elif target > nums[mid] and target < nums[0]:
                low = mid + 1
            # 当向前规约时
            else:
                high = mid
        if low == high and nums[low] == target:
            return nums.index(target)
        else:
            return -1
