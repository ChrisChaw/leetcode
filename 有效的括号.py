class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'}':'{', ')':'(', ']':'['}
        for ch in s:
            if ch in {'(','[','{'}:
                stack.append(ch)
            elif len(stack) > 0:
                if match[ch] == stack[-1]: # 与栈顶元素相匹配 如果能匹配就出栈
                    stack.pop()
                else: # 与栈顶元素相匹配 如果不能匹配 字符串无效
                    return False
            else: # len(stack) == 0 如果字符串里没有右括号 字符串无效
                return False
        if len(stack) == 0: # 最后 栈为空了 说明字符串有效
            return True
        else: # 最后 栈不为空 说明字符串无效
            return False