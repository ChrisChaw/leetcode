class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
        for i in range(0, len(s) + 1):
            dp[0][i] = 1  # 只要前者t为空 不管s为多少 在s中t出现的次数为1
        for i in range(1, len(t) + 1):
            for j in range(i, len(s) + 1):
                # 当S[j]==T[i], i和j可以都往前挪一位 或者i不动，j往前挪一位
                # 当S[j] != T[i], i和j不可以都往前挪一位, i不动，j往前挪一位 因为j是S里面的 所以j可以任意地挪掉
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
