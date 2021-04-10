"""
算是一道比较经典的回溯题了，首先建立backtrace函数，有两个参数，一个是从1开始一直加到n的整数，一个是暂存的列表。
先用一个if语句判断回溯结束条件，就是列表的长度是否等于k，如果是的话就添加进res中，然后结束递归函数。
如果列表长度小于k的话，就进入循环，将j增大1，且暂存列表加入数字j。
全部结束完输出结果res即可。
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrace(i, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrace(j + 1, tmp + [j])

        backtrace(1, [])
        return res
