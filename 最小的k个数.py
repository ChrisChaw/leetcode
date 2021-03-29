class Solution:  # 时间复杂度:O(n)
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return None
        if k == 0:
            return []
        low, high = 0, len(arr) - 1
        while True:
            pos = self.partition(arr, low, high)
            if pos == k - 1:
                return arr[:k]
            elif pos > k - 1:
                high = pos - 1
            else:
                low = pos + 1

    def partition(self, arr, low, high):
        pivot = arr[low]
        while low < high:
            while low < high and pivot <= arr[high]:
                high -= 1
            arr[low] = arr[high]
            while low < high and pivot > arr[low]:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot  # 或者 arr[high] = pivot
        return low
