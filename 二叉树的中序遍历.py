class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        get_node = root
        while get_node or len(stack):
            if get_node:
                stack.append(get_node)
                get_node = get_node.left
            else:
                get_node = stack.pop()
                result.append(get_node.val)
                get_node = get_node.right
        return result

"""
其核心思想如下：
使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
(因为栈是先进后出的 而中序遍历是:左根右 所以入栈顺序是:右根左)
如果遇到的节点为灰色，则将节点的值输出。
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
