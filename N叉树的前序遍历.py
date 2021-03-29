"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = list()
        for leaf in root.children:
            res += self.preorder(leaf)
        return [root.val] + res
