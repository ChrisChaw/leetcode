class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root == None:
            return result
        stack = list()
        stack.append(root)
        while len(stack) != 0:
            top = stack.pop()
            if top.right != None:
                stack.append(top.right)
            if top.left != None:
                stack.append(top.left)
            result.append(top.val)
        return result
