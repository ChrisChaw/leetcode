class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        la = len(text1)
        lb = len(text2)
        res = [[0 for i in range(lb + 1)] for j in range(la + 1)]
        for i in range(1, la + 1):
            for j in range(1, lb + 1):
                if text1[i - 1] == text2[j - 1]:
                    res[i][j] = res[i - 1][j - 1] + 1
                else:
                    res[i][j] = max(res[i][j - 1], res[i - 1][j])
        return res[-1][-1]
