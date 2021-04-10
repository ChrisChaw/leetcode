# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 用队列queue实现一个BFS
        if root is None:
            return []
        queue = [root]  # 把root初始化放到队列里
        res = []  # res存储最终结果
        while queue:
            import sys
            max_val = -sys.maxsize
            child = []  # 存储一层循环中该层的结果
            node = []  # 存放下一层(左孩子或右孩子)的结果
            for item in queue:  # 将该层queue里的数据循环一遍 存到child里
                child.append(item.val)
                if item.left:  # 如果该层节点的左孩子有值 就把它的左孩子存到下一层node里
                    node.append(item.left)
                if item.right:  # 如果该层节点的右孩子有值 就把它的右孩子存到下一层node里
                    node.append(item.right)
            max_val = max(max_val, max(child))
            res.append(max_val)  # 把一层最大值的结果存在res里
            queue = node  # 把下一层结果node赋给queue 下次循环时 作为当前层来处理
        return res
