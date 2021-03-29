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
