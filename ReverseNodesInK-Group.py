# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = ListNode(0)
        p.next = head
        head = p
        s = p
        leng = k
        while k > 0 and s != None:
            k -= 1
            s = s.next
        while s != None:
            flag = s.next
            tail = p.next
            l = p.next
            while l != flag:
                tmp = p.next
                p.next = l
                l = l.next
                p.next.next = tmp
            tail.next = l
            p = tail
            s = tail
            k = leng
            while k > 0 and s != None:
                k -= 1
                s = s.next
        return head.next
