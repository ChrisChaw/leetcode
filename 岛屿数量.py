class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0  # 记录岛屿个数 先初始化为0
        m = len(grid)  # 记录 行数
        if m == 0:
            return 0
        n = len(grid[0])  # 记录 列数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 如果是陆地 就把陆地本身 及周围陆地 移为 水
                    self.DFSMarking(grid, i, j, m, n)
                    # 岛屿个数+1
                    count += 1
        return count

    def DFSMarking(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.DFSMarking(grid, i + 1, j, m, n)
        self.DFSMarking(grid, i - 1, j, m, n)
        self.DFSMarking(grid, i, j + 1, m, n)
        self.DFSMarking(grid, i, j - 1, m, n)
