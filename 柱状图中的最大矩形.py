class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n  # left,right: 元素的左右边界

        stack = list()  # 待维护的栈
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:  # 如果维护的栈不为空 且 当前元素的值<=栈顶元素的值
                right[stack[-1]] = i  # 保存当前元素的索引为栈顶元素的右边界
                stack.pop()  # 弹出栈顶元素 下一个元素变成栈顶元素了
            # 如果栈不为空:栈顶元素为当前元素i的左边界; 如果栈为空:左边界为-1
            left[i] = stack[-1] if stack else -1
            stack.append(i)  # 当前元素i入栈
        # 面积 = 当前元素高度 * (当前元素右边界-当前元素左边界-offset)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
