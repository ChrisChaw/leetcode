class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def build_tree_from_inorder_and_postorder(inorder: List[int], postorder: List[int]) -> Node:
        if not (postorder and inorder):
            return None

        root = Node(postorder[-1])

        mid_inx = inorder.index(root)

        root.left = self.build_tree_from_inorder_and_postorder(inorder[:mid_inx], postorder[:mid_inx])

        root.right = build_tree_from_inorder_and_postorder(inorder[mid_inx + 1:], postorder[mid_inx:-1])
