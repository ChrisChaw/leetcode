class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        方法一：回溯
        当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
        定义函数 backtrack(combination, nextdigit)，当 nextdigit 非空时，
        对于 nextdigit[0] 中的每一个字母 letter，执行回溯 backtrack(combination + letter,nextdigit[1:]，
        直至 nextdigit 为空。最后将 combination 加入到结果中。
        """
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        方法二：队列
        我们也可以使用队列，先将输入的 digits 中第一个数字对应的每一个字母入队，
        然后将出队的元素与第二个数字对应的每一个字母组合后入队...直到遍历到 digits 的结尾。
        最后队列中的元素就是所求结果。
        """
        if not digits: return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码 0的ASCII码是48 依此类推
                    queue.append(tmp + letter)
        return queue
