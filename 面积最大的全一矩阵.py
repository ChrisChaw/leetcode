"""
问题：设一个矩阵全部由0和1组成，求该矩阵M中只包含1的最大正方形的面积

分析：假设为矩阵上面坐标(i,j)的点的值。假设表示以坐标点(i,j)的为右下角的正方形的边长，那么很容易可以知道如下规律：

如果为0，则为0；

如果不为0，则的值等于以点(i-1,j-1)、点(i-1,j)和点(i,j-1)为右下角的所组成的正方形的最小边长+1；

同时，矩阵D的第一列和第一行的值直接等于矩阵M的值（区分0，1）。
"""


def maximalSquare(matrix):
    if matrix == []:
        return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(N)] for _ in range(M)]
    Max = 0
    for i in range(N):  # dp矩阵初始化
        dp[0][i] = int(matrix[0][i])
        Max = max(dp[0][i], Max)
    for i in range(M):  # dp矩阵初始化
        dp[i][0] = int(matrix[i][0])
        Max = max(dp[i][0], Max)
    for i in range(1, M):
        for j in range(1, N):
            if matrix[i][j] == '0':
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            Max = max(dp[i][j], Max)
    return Max ** 2
