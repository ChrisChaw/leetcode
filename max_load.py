import numpy as np
import sys
import math


# 仓库节点
class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# 最优路径搜索
class maxOptimalPath:
    """
    参数:
    时间转移矩阵：T
    卡车行驶速度：Vs
    初始货量：init_volume
    指数常数：exp_cons
    """

    def __init__(self, warehouses, speed, init_volume, exp_cons, origin=Node(), eps=None, capacity=None):
        assert len(warehouses) > 0  # 必须至少到一个仓库
        self.vectors = [[w.x, w.y] for w in warehouses]  # 仓库节点坐标
        self.vecors.insert(0, [origin.x, origin.y])  # 原点
        self.T = np.zeros((len(self.vectors), len(self.vectors)), dtype=np.float)  # 初始化时间状态转移矩阵T为全0方阵
        self.Vs = speed  # 卡车速度
        self.init_volume = init_volume  # 初始货量
        self.exp_cons = exp_cons  # 常数
        self.capacity = capacity  # 卡车装货总量
        self.best_path, self.max_load = self.Viterbi()  # Viterbi算法得到最佳路径及其最大装货量

    # 仓库存量
    def Stock(self, V0, lamda, t):
        return V0 * np.exp(-lamda * t)

    def Viterbi(self):
        # 给定仓库坐标，用Viterbi算法找到可以实现最大装货量的路径
        n_vectors = len(self.vectors)
        # 时间转移矩阵T
        for i in range(n_vectors):
            for j in range(n_vectors):
                if i == j:
                    self.T[i][j] = 0
                else:
                    self.T[i][j] = math.sqrt((self.vectors[j][0] - self.vectors[i][0]) ** 2 + (
                            self.vectors[j][1] - self.vectors[i][1]) ** 2) / Vs
        # 记录动态规划存储矩阵dp、最佳路径的回溯矩阵traces、时间流逝矩阵time_pass、经过的仓库（节点）node_passed
        dp = np.zeros((n_vectors, n_vectors - 1), dtype=float)  # shape：[n_vectors,n_vectors-1]
        traces = np.zeros((n_vectors, n_vectors - 1), dtype=int)
        time_pass = np.zeros((n_vectors, n_vectors - 1), dtype=float)
        node_passed = [[[0] * n_vectors for _ in range(n_vectors)] for _ in
                       range(n_vectors)]  # shape: [n_vectors,n_vectors,n_vectors]
        # 初始化第一个路径的装货量 以及 相应流逝的时间
        for i in range(n_vectors):
            # 跳过起始点
            if i == 0:
                continue
            # 0号仓库 的i状态（库存量）
            dp[i][0] = self.Stock(self.init_volume[i - 1], self.exp_cons[i - 1], self.T[i][0])
            time_pass[i][0] = self.T[i][0]
        # 动态规划从第二个路径开始
        for t in range(1, n_vectors - 1):
            for i in range(n_vectors):
                # 当前节点回溯最佳路径
                current_best_path = [0] * n_vectors
                # 跳过起始点，以及经过的点
                if i == 0:
                    continue
                dp[i][t] = -sys.maxsize  # 初始值为系统最小值
                for k in range(n_vectors):
                    # 路径不会回到起始点，不会经过自己，且 不经过上一个节点所存储的经过的路径
                    if k == 0 or k == i or k in node_passed[k][t - 1]:
                        continue
                    # 到当前节点(状态是i) 时间流逝的叠加
                    tp = time_pass[k][t - 1] + self.T[k][i]
                    # 卡车当前的装货量(状态i) 从t-1号仓库的状态k--->t号仓库的状态i
                    score = dp[k][t - 1] + self.Stock(self.init_volume[k - 1], self.exp_cons[k - 1], tp)
                    # 更新dp
                    if score > dp[i][t]:
                        dp[i][t] = score  # 动态规划存储矩阵的元素dp[i][t]表示卡车跑到当前节点（仓库）的最佳路径值
                        traces[i][t] = k  # 回溯矩阵的元素traces[i][t]表示当前节点最佳路径的上一个节点是哪一个
                        time_pass[i][t] = tp  # 时间流逝矩阵的元素time_pass[i[[t]表示卡车跑到当前节点t 所经历的时间
                # 到当前仓库t的最佳路径
                current_best_path[t] = traces[i][t]  # 存储的是：第t个节点的货物量

                for x in range(t - 1, 0, -1):
                    # 由于当前时刻节点x的traces[i][x]表示来自上一时刻节点x-1
                    # 而现在可以用i=np.argmax(dp[:][x])得到x-1时刻的最佳路径的下标位置
                    current_best_path[x] = traces[np.argmax(dp[:][x]), x]
                # 把当前节点t经过的路径存储到node_passed[i][t]
                node_passed[i][t] = current_best_path
                max_stock = dp[current_best_path[t], t - 1]

                # 如果有指定卡车的最大容量self.capacity 判断装货量是否超过该容量
                if self.capacity and dp[i][t] >= self.capacity:
                    return current_best_path, max_stock
        # 回溯最佳路径
        best_path = [0] * n_vectors
        # 从倒数最佳路径的倒数第二个循环
        for t in range(n_vectors - 2, 0, -1):
            # 由于当前节点t的traces[i][t]表示来自上一时刻t-1的哪个节点
            # 现在可以用i = np.argmax(dp[:][t])得到t-1时刻的最佳路径的下标位置
            # 又因为best_path的列数列数比dp多一列 所以 得到扽下标位置放在t处
            best_path[t] = traces[np.argmax(dp[:][t])][t]
        # 最佳路径的最后一个元素p 先初始化
        p = -sys.maxsize
        for i in range(len(dp[:][-1])):
            # 如果最后一个元素dp[i][-1]没有在最佳路径里 且>之前的最后一个元素p 更新最后一个元素p和最佳路径的最后一个元素best_path[-1]
            if dp[i][-1] > p and i not in best_path:
                p = dp[i][-1]
                best_path[-1] = i
        max_load = dp[best_path[-1], -1]

        return best_path, max_load
