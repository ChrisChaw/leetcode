# 定义节点
class SNode:
    Next = None
    Value = None


# 创建带头结点的链表
def createLinkList(size):
    if size <= 0:
        return None
    linkList = SNode()
    pNode = linkList
    # 尾插法
    for i in range(1, size + 1):
        node = SNode()
        node.Value = i
        pNode.Next = node
        pNode = pNode.Next
    return linkList


# 打印链表
def printLinkList(linkList):
    if linkList == None:
        print('None')
        return
    s = "head"
    node = linkList.Next
    while node != None:
        s = s + "->" + str(node.Value)
        node = node.Next
    print(s)
    return s


# 翻转链表从m到n的位置
# 假定给出的参数满足：1≤m≤n≤链表长度，下面就不做参数验证了
def reverseLinkList(linkList, m, n):
    '''
    先找到第m个元素，然后把链表中的第n个元素添加到它前面，重复执行n-m次
    如：给定1→2→3→4→5，m=2，n=4，
    head->1->2->3->4->5
    head->1->4->2->3->5 把4插入到2前面
    head->1->4->3->2->5 把3插入到2前面
    '''

    # 第m个元素的前节点
    preMNode = linkList
    for i in range(m - 1):
        preMNode = preMNode.Next

    for i in range(n - m):
        # 找到第n个节点的前节点
        preNNode = linkList
        for j in range(n - 1):
            preNNode = preNNode.Next
        # 找到第n个节点
        nNode = preNNode.Next
        preNNode.Next = preNNode.Next.Next
        # 把第n个节点加到第m个节点之前
        # 把第m个节点赋值给第n个节点的next
        nNode.Next = preMNode.Next
        # 把第n个节点赋值给第m个节点
        preMNode.Next = nNode
        # m节点指向下一个节点（后移一位）
        preMNode = preMNode.Next
        printLinkList(linkList)


if __name__ == '__main__':
    linkList = createLinkList(10)
    printLinkList(linkList)
    print(reverseLinkList(linkList, 3, 6))
