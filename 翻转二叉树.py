class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归法
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


class Solution:
    def invertTree(self, root):
        if not root:
            return None
        # 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        queue = [root]
        while queue:
            # 每次都从队列中拿一个节点，并交换这个节点的左右子树
            tmp = queue.pop(0)
            tmp.left, tmp.right = tmp.right, tmp.left
            # 如果当前节点的左子树不为空，则放入队列等待后续处理
            if tmp.left:
                queue.append(tmp.left)
            # 如果当前节点的右子树不为空，则放入队列等待后续处理
            if tmp.right:
                queue.append(tmp.right)
            # 返回处理完的根节点
        return root
