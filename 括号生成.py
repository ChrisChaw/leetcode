# 方法一
class Solution:
    def generate(p, left, right, parens=[]):
        """
        p是到目前为止构建的括号字符串，left,right指示仍要添加的左右括号的数量，parens收集括号
        """
        if left:
            generate(p + '(', left - 1, right)  # 已经添加了一个左括号了 left-1
        if right > left:
            generate(p + ')', left, right - 1)  # 已经添加了一个right括号了 right-1
        if not right:
            parens += p,
        return parens

    return generate('', n, n)


# 方法2
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right): yield q
                for q in generate(p + ')', left, right - 1): yield q

        return list(generate('', n, n))


# 方法3（方法2的改进）
class Solution:
    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)] + \
                   [')' + p for p in self.generateParenthesis(n, open - 1)]
        return [')' * open] * (not n)
