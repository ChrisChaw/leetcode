class Solution:
    def mySqrt(self, x: int) -> int:
        # 方法1:二分查找
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        mid = 1
        while left <= right:
            mid = (right + left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right  # left与right交汇了


class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿法
        if x < 0:
            return Exception('不能输入负数')
        if x == 0:
            return 0
        # 迭代的初始值 随意设置 假设设置为1
        cur = 1
        while True:
            # 前一次的值为pre
            pre = cur
            # 迭代公式
            cur = (cur + x // cur) // 2
            if abs(cur - pre) < 1e-6:
                return cur


class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿法
        r = x  # 迭代的初始值设为x
        while r * r > x:  # 当r*r<=x时，说明第一次到达了x的平方根的整数 返回结果
            # 迭代公式
            r = (r + x // r) // 2
        return r
