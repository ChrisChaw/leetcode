class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 用队列queue实现一个BFS
        if root is None:
            return []
        queue = [root]  # 把root初始化放到队列里
        res = []  # res存储最终结果
        while queue:
            child = []  # 存储一层循环中该层的结果
            node = []  # 存放下一层(左孩子或右孩子)的结果
            for item in queue:  # 将该层queue里的数据循环一遍 存到child里
                child.append(item.val)
                if item.left:  # 如果该层节点的左孩子有值 就把它的左孩子存到下一层node里
                    node.append(item.left)
                if item.right:  # 如果该层节点的右孩子有值 就把它的右孩子存到下一层node里
                    node.append(item.right)
            res.append(child)  # 把一层的结果存在res里
            queue = node  # 把下一层结果node赋给queue 下次循环时 作为当前层来处理
        return res


# DFS实现层序遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []  # 存储最终结果
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root:
            return
        if len(res) == level:  # res里有几个列表就代表有几层(多少深度)
            res.append([])
        res[level].append(root.val)  # 根节点存放到第0层
        if root.left:  # 如果左孩子有值 递归对左孩子做同样处理 层数+1
            self.level(root.left, level + 1, res)
        if root.right:  # 如果右孩子有值 递归对右孩子做同样处理 层数+1
            self.level(root.right, level + 1, res)
