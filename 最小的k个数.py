class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        方法：k个数的大根堆
        思路和算法：
        我们用一个大根堆实时维护数组的前 k 小值。首先将前 k 个数插入大根堆中，随后从第 k+1 个数开
        始遍历，如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。最后将大
        根堆里的数存入数组返回即可。在下面的代码中，由于 C++ 语言中的堆（即优先队列）为大根堆，我们可以这
        么做。而 Python 语言中的堆为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前
        k个最小值。

        复杂度分析:
        时间复杂度：O(nlogk)，其中 n 是数组 arr 的长度。由于大根堆实时维护前 k 小值，所以插入删除都是 O(logk) 的时间复杂度，
        最坏情况下数组里 n 个数都会插入，所以一共需要O(nlogk) 的时间复杂度。
        空间复杂度：O(k)，因为大根堆里最多 k 个数。
        """
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        import heapq
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if arr[i] < -hp[0]:
                heapq.heappop(hp)  # hp必须是个list,pop出第一个元素
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


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
