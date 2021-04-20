class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        ret = 0
        for i in range(0, len(isConnected)):
            if not visited[i]:
                self.dfs(isConnected, visited, i)
                ret += 1
        return ret

    def dfs(self, m, visited, i):
        for j in range(0, len(m[i])):
            if m[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(m, visited, j)
