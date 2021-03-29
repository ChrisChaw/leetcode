# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        while p is not None and p.next is not None:  # 前后都存在
            tmp = p.val  # 前一个值a,给t
            p.val = p.next.val  # 后一个值b,给a
            p.next.val = tmp  # t再给b
            p = p.next.next
        return head
