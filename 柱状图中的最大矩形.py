class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈
        heights.append(0)
        stack = [0]
        area = 0
        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]:  # 当前元素大于栈顶元素 则当前元素的索引入栈
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    # 栈非空 且 当前元素小于栈顶元素 弹出栈顶元素(索引) 此时计算以该元素(索引)的高为高的最大矩形
                    x = stack.pop(-1)
                    if len(stack) != 0:
                        area = max(area, heights[x] * (i - stack[-1] - 1))
                    else:
                        area = max(area, heights[x] * i)
                stack.append(i)
        return area
