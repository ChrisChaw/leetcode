class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        贪心思想：先满足胃口小的孩子
        先对孩子胃口和饼干尺寸分别排序
        遍历孩子胃口和饼干尺寸
        胃口比饼干尺寸小，返回值res + 1，继续遍历下一个孩子(i + 1)和下一块饼干(j + 1)
        胃口比饼干尺寸大，遍历下一块饼干(j + 1)
        复杂度分析：
        时间复杂度：O(mlogm + nlogn)，排序费时费空间
        空间复杂度：O(logm + logn)
        """
        g.sort()
        s.sort()
        i = j = res = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                res += 1
            j += 1
        return res
