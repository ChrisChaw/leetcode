class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.result = []
        # 之前的皇后所攻击的位置 (列 pie na)
        self.cols = set()
        self.pie = set()
        self.na = set()

        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # 递归终止条件
        if row >= n:  # 一行放置一个皇后
            self.result.append(cur_state)
            return
        # 当前层
        for col in range(n):  # 遍历到column
            # 如果放置的位置与之前的皇后冲突 略过
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            # 更行flags
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])
            # reverse states
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i:i + n] for i in range(0, len(board), n)]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_dif, xy_sum):
            # 传3个参数 每一行的第几列是皇后 该皇后位置的行号与列号之和 之差 分别代表撇和捺的位置
            p = len(queens)  # 行号
            if p == n:
                result.append(queens)
                return
            for q in range(n):  # 列号
                # 对于每一行的列号进行循环 如果该列号不在三个参数里 就更新三个参数 该位置可以放一个皇后
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        dfs([], [], [])
        # result里放的依次是每一行皇后所在列 对于答案里的每一个列号 前面放点 后面放点 本身放Q
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
