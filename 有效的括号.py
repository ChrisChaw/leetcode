class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'}': '{', ')': '(', ']': '['}
        for ch in s:
            if ch in {'(', '[', '{'}:
                stack.append(ch)
            elif len(stack) > 0:
                if match[ch] == stack[-1]:  # 匹配就出栈
                    stack.pop()
                else:
                    return False
            else:  # len(stack) == 0
                return False
        if len(stack) == 0:
            return True
        else:
            return False
