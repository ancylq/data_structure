# coding:utf-8
'''
树是节点的有限集合
节点的度是节点孩子的个数
节点的深度即节点所在的层数

索引从0开始，父节点表示为(i-1)/2，则i*2+1为左孩子，i*2+2为右孩子，最后一个非叶子节点的索引为：叶子个数/2
索引从1开始，父节点表示为i/2，则i*2为左孩子，i*2+1为右孩子，最后一个非叶子节点的索引为：(叶子个数-1)/2

下面的例子索引从0开始。
'''
class MyBinaryTreeArray(object):
    def __init__(self, size, pRoot):
        self.m_pTree = [None] * size
        self.m_pTree[0] = pRoot
        self.m_iSize = size

    def __del__(self):
        del self.m_pTree
        self.m_pTree = None

    def searchNode(self, nodeIndex):
        if nodeIndex<0 or nodeIndex>=self.m_iSize:
            return 
        if self.m_pTree[nodeIndex] == None:
            # 值为None，则无该节点
            return
        return self.m_pTree[nodeIndex]
        

    def addNode(self, nodeIndex, direction, pNode):
        '''
        nodeIndex  要插入节点的父节点索引
        direction  要插入点是父节点的左孩子(0)还是右孩子(1)
        pNode      要插入的节点
        '''
        if nodeIndex<0 or nodeIndex>=self.m_iSize:
            return False
        if not self.m_pTree[nodeIndex]:
            return False

        if direction == 0:
            if nodeIndex*2+1 >= self.m_iSize:
                return False
            if self.m_pTree[nodeIndex*2+1] != None:
                return False
            self.m_pTree[nodeIndex*2+1] = pNode

        if direction == 1:
            if nodeIndex*2+2 >= self.m_iSize:
                return False
            if self.m_pTree[nodeIndex*2+2] != None:
                return False
            self.m_pTree[nodeIndex*2+2] = pNode

    def deleteNode(self, nodeIndex):
        '''
        删除结点时应该一并删除其所有子节点以及后续子节点，程序未考虑
        '''
        if nodeIndex<0 or nodeIndex>=self.m_iSize:
            return False

        if self.m_pTree[nodeIndex] == None:
            return False

        pNode = self.m_pTree[nodeIndex]
        self.m_pTree[nodeIndex] = None
        return pNode

    def treeTraverse(self):
        for i in self.m_pTree:
            print i

if __name__ == '__main__':
    pTree = MyBinaryTreeArray(10, 3)
    
    print '----------Insert into node ----------'
    pTree.addNode(0, 0, 5) # 左孩子为5
    pTree.addNode(0, 1, 8) # 右孩子为8

    pTree.addNode(1, 0, 2)
    pTree.addNode(1, 1, 6)
    
    pTree.addNode(2, 0, 9)
    pTree.addNode(2, 1, 7)
    
    pTree.treeTraverse()
    print '----------node value which nodeIndex is 2 ----------'
    print pTree.searchNode(2) # 搜索nodeIndex为2的节点的值
    print '----------delete node which nodeIndex is 6 and show deleted node value ----------'
    print pTree.deleteNode(6) # 删除nodeIndex为7的节点
    print '----------traverse tree after delete node ----------'
    pTree.treeTraverse()
