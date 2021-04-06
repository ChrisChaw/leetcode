import re


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = s.strip()  # 清除两边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')  # 设置正则规则
        num = num_re.findall(str)  # 查找匹配的内容
        num = int(*num)  # 由于返回的是个列表，解包并且转换成整数
        return max(min(num, INT_MAX), INT_MIN)  # 返回值
