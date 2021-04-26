class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):  # 从倒数第2行逆序遍历
            for j in range(len(triangle[i])):  # 正序遍历列
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return dp[0][0]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # mini:开一个最大行数的数组
        # dp[i][j] = triangle[i][j] + min(dp [i+1][j], dp[i+1][j+1])
        mini, M = triangle[-1], len(triangle)
        for i in range(M - 2, -1, -1):  # 从倒数第2行逆序遍历
            for j in range(len(triangle[i])):  # 正序遍历列
                mini[j] = triangle[i][j] + min(mini[j], mini[j + 1])
        return mini[0]
