import sys


def minCoins(coins, m, C):
    """
    :param coins: list 存硬币的面值
    :param m: 硬币的个数 = len(coins)
    :param C: 需要换的纸币面值
    :return:
    """
    # M[j]:存储换取面值为j的纸币，需要用到的最少量的硬币数目
    M = [0 for i in range(C + 1)]
    M[0] = 0
    # 初始化
    for i in range(1, C + 1):
        M[i] = sys.maxsize
    # 对于每一种价值j来计算，最少用多少硬币可以换取？
    for j in range(1, C + 1):
        # 遍历所有比面值j小的硬币coins[i]
        for i in range(m):
            if coins[i] <= j:
                # 如果剩余面值的数量小于当前面值的数量
                if M[j - coins[i]] < M[j] and M[j - coins[i]] != sys.maxsize:
                    M[j] = M[j - coins[i]] + 1
    if M[C] == sys.maxsize:
        return -1
    else:
        return M[C]
