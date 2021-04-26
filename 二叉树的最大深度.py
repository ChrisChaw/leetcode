# 非递归版本
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        if root == None:
            return ans
        st = []  # 栈
        st.append(root)
        gp = st[0]  # gp为指向每层最后一个节点的指针
        ans += 1  # ans表示层数
        while len(st) != 0:
            tmp = st[0]
            if tmp.left != None:
                st.append(tmp.left)
            if tmp.right != None:
                st.append(tmp.right)
            # 遇到每层最后一个往后移 层数+1
            if gp == tmp:
                gp = st[len(st) - 1]
                if gp != st[0]:
                    ans += 1
            st.pop(0)  # 把0号索引处的值出栈
        return ans


# 递归版本
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
