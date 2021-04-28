def check_brack(exp):
    stack = []
    match = {'}': '{', ']': '[', ')': '('}
    for ch in exp:
        if ch in {'(', '[', '{'}:  # 遇到右括号 就进栈
            stack.append(ch)
        elif len(stack) > 0:
            if match[ch] == stack[-1]:  # 遇到左括号 就出栈
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False
