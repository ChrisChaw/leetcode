class Solution:
    def isBalanced_Solution(self, pRoot):
        return self.dfs(pRoot) != -1

    def dfs(self, p):
        if p == None:
            return 0
        left = self.dfs(p.left)
        # 先判断左子树是否是平衡二叉树 如果是 再判断右子树是否是平衡二叉树 如果不是平衡树，直接返回-1层层跳出递归直到他的根节点
        if left == -1:
            return -1
        right = self.dfs(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:  # 执行到这一步，说明左右子树都是平衡二叉树，在判断在整体是不是二叉树，不是返回-1
            return -1
        return max(left, right) + 1  # 如果子树是平衡二叉树，则返回子树的高度
