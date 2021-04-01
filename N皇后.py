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
