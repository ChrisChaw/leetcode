class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归法 时间复杂度O(n) 空间复杂度O(n) n:节点个数
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True
            val = node.val  # 记录当前节点的值
            if val <= lower or val >= upper:  # 如果当前节点的值不在上下界内:不合理二叉树
                return False
            if not helper(node.right, val, upper):  # 递归调用右子树 当前节点的值作为下界
                return False
            if not helper(node.left, lower, val):  # 递归调用左子树 当前节点的值作为上界
                return False
            return True

        return helper(root)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历法 时间复杂度：O(n) 空间复杂度：O(n) n:节点个数
        stack, inorder = [], float('-inf')  # 栈，记录遍历过的节点
        while stack or root:  # 栈里有值或根节点有值
            while root:  # 根节点有值
                stack.append(root)  # 把根节点压入栈
                root = root.left  # 先把根节点的左孩子当成下一个根节点 循环入栈
            root = stack.pop()  # 把这些入栈的‘根’节点取出 记为root节点
            # 如果中序遍历得到的节点的值root<=上一个遍历过的值inorder 说明不是二叉搜索树 因为二叉搜索树是个升序
            if root.val <= inorder:
                return False
            inorder = root.val  # 记录一下root这个节点被遍历过了 记为inorder
            root = root.right  # 再循环操作节点的右孩子
        return True
