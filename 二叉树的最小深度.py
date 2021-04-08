class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        if left_height != 0 and right_height != 0:
            return min(left_height, right_height) + 1
        elif left_height == 0:
            return right_height + 1
        elif right_height == 0:
            return left_height + 1
