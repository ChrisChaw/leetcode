class Solution:
    # def reverseBits(self, n: int) -> int:
    #     ans, MASK = 0, 1
    #     for i in range(32):
    #         if n & MASK:
    #             ans |= 1 << (31-i)
    #         MASK <<= 1
    #     return ans

    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res * 2 + n % 2
            n = n // 2
        return res
