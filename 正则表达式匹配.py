class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            # 发现'*'通配符
            # 如果发现有字符和'*'结合
            # 或者匹配该字符0次，然后跳过该字符(p[0])和跳过'*':self.isMatch(s, p[2:])
            # 或者当p[0]和s[0]匹配后，移动text: first_match and self.isMatch(s[1:], p)
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()  # 备忘录

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
