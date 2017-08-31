# coding:utf-8
'''
单向链表
'''
class Node(object):
    __slots__ = ('data', 'next')
    
    def printNode(self):
        print self.data

class MySinglyLinkedList(object):

    def __init__(self):
        self.m_pList = Node() 
        self.m_pList.data = 0  
        self.m_pList.next = None
        self.m_iLength = 0    # 表中实际元素个数

    def __del__(self):
        '''
        将所有的节点都释放掉
        '''
        self.clearList()
        del self.m_pList
        self.m_pList = None

    def clearList(self):
        '''
        除了第一个节点设为默认值外，其他节点都释放掉
        '''
        currentNode = self.m_pList.next
        while currentNode != None:
            temp = currentNode.next
            del currentNode
            currentNode = temp

        self.m_pList.next = None

    @property
    def listEmpty(self):
        return True if self.m_iLength == 0 else False

    @property
    def listLength(self):
        return self.m_iLength

    def listInsertHead(self, pNode):
        temp = self.m_pList.next
        newNode = Node()
        if newNode == None:
            '''内存申请失败'''
            return False
        newNode.data = pNode.data
        self.m_pList.next = newNode
        newNode.next = temp
        self.m_iLength += 1
        return True

    def listInsertTail(self, pNode):
        currentNode = self.m_pList
        while currentNode.next != None:
            currentNode = currentNode.next
        # 因为pNode是可变对象，为了避开浅拷贝问题，就重新实例化了
        newNode = Node()
        if newNode == None:
            '''内存申请失败'''
            return False
        newNode.data = pNode.data
        newNode.next = None
        currentNode.next = newNode
        self.m_iLength += 1
        return True

    def listInsert(self, i, pNode):
        '''
        i=0 插入头节点后面
        i=m_iLength 插入最后面
        '''
        if i<0 or i>self.m_iLength:
            return False

        currentNode = self.m_pList
        for k in range(i):
            currentNode = currentNode.next
        newNode = Node()
        if newNode == None:
            return False
        newNode.data = pNode.data
        # 下面两行顺序不能变
        newNode.next = currentNode.next
        currentNode.next = newNode
        self.m_iLength += 1
        return True

    def listDelete(self, i, pNode):
        if i<0 or i>=self.m_iLength:
            return False
        currentNode = self.m_pList
        currentNodeBefore = None
        for k in range(i+1):
            currentNodeBefore = currentNode
            currentNode = currentNode.next

        currentNodeBefore.next = currentNode.next
        pNode.data = currentNode.data 
        del currentNode
        currentNode = None
        self.m_iLength -= 1
        return True

    def getElem(self, i):
        ''' 获取元素'''
        if i<0 or i>=self.m_iLength:
            return False
        currentNode = self.m_pList
        currentNodeBefore = None
        for k in range(i+1):
            currentNodeBefore = currentNode
            currentNode = currentNode.next
        return currentNode.data

    def locateElem(self, pNode):
        ''' 定位元素位置'''
        currentNode = self.m_pList
        count = 0
        while current.next != None:
            currentNode = currentNode.next
            if currentNode.data == pNode.data:
                return count
            count += 1
        return -1

    def priorElem(self, pCurrentNode):
        ''' 获取前驱元素'''
        currentNode = self.m_pList
        tempNode = None
        count = 0
        while currentNode.next !=None:
            tempNode = currentNode
            currentNode = currentNode.next
            if currentNode.data == pCurrentNode.data:
                if tempNode == self.m_pList:
                    # tempNode是第一个节点
                    return False
#                 pPreNode.data = tempNode.data
                return tempNode.data
        return False

    def nextElem(self, pCurrentNode):
        ''' 获取后继元素'''
        currentNode = self.m_pList
        while currentNode.next != None:
            currentNode = currentNode.next
            if currentNode.data == pCurrentNode.data:
                if currentNode.next == None:
                    return False
#                 pNextNode.data = currentNode.next.data
                return currentNode.next.data
        return False

    def listTraverse(self):
        currentNode = self.m_pList
        while currentNode.next != None:
            # 头节点的data域无用
            currentNode = currentNode.next
            currentNode.printNode()

def main():
    node1 = Node()
    node1.data = 3
    node2 = Node()
    node2.data = 4
    node3 = Node()
    node3.data = 5
    node4 = Node()
    node4.data = 6
    
    pList = MySinglyLinkedList()

    print '----- list insert head -----'
     
    pList.listInsertHead(node1)
    pList.listInsertHead(node2)
    pList.listInsertHead(node3)
    pList.listInsertHead(node4)
 
    pList.listTraverse() # 6543

    print '----- list insert tail -----'
    pList.listInsertTail(node1)
    pList.listInsertTail(node2)
    pList.listInsertTail(node3)
    pList.listInsertTail(node4)

    pList.listTraverse() # 65433456

    node5 = Node()
    node5.data = 7
    print '----- insert the number 7 in 0 -----'
    pList.listInsert(0, node5)
    pList.listTraverse() # 765433456
    print '----- insert the number 7 in 4 -----'
    pList.listInsert(4, node5)
    pList.listTraverse() # 7654733456
    
    print '----- delete number 7 in 0 -----'
    print pList.listDelete(0, node5) # 7
    pList.listTraverse() #654733456

    print pList.getElem(3) # 7
    print pList.priorElem(node5) # 4
    print pList.nextElem(node5) # 3

    del pList


main()
