class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n-1, -1, -1): # 枚举起点 从尾到头
            for j in range(i, n): # 枚举终点 从i后面开始
                dp[i][j] = s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]) # dp[i+1][j-1]: 它的子串是回文串; s[i] == s[j]:第i个字符与第j个字符相同
                if dp[i][j] and j-i+1 > len(res):
                    res = s[i:j+1]
        return res
