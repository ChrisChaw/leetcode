class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == '' or len(strs) == 0:
            return ""
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):  # 第j个字符串
                if i == len(strs[j]) or strs[j][i] != c:  # i:第j个字符串的长度 strs[j][i]:第j个字符串的第i个字符
                    return strs[0][:i]  # 如果在第i个字符处不相同了
        return strs[0]
