class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x, n = 1.0 / x, -n
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        elif n % 2 == 1:
            half = self.myPow(x, n // 2)
            return half * half * x
