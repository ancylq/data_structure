# coding:utf-8
'''
图的存储（邻接矩阵）与图的遍历（深度优先、广度优先）

例：
    A                A B C D E F G H
   /  \           A    1   1               [0, 1, 0, 1, 0, 0, 0, 0,
  B    D          B  1   1     1            1, 0, 1, 0, 0, 1, 0, 0,
 / \  / \    ==>  C    1     1         ==>  0, 1, 0, 0, 1, 0, 0, 0,
C   F G--H        D  1           1 1        1, 0, 0, 0, 0, 0, 1, 1,
 \ /              E      1     1            0, 0, 1, 0, 0, 1, 0, 0,
  E               F    1     1              0, 1, 0, 0, 1, 0, 0, 0,
                  G        1       1        0, 0, 0, 1, 0, 0, 0, 1,
                  H        1     1          0, 0, 0, 1, 0, 0, 1, 0]
'''
class Node(object):
    
    def __init__(self, data=0):
        self.m_cData = data
        self.m_bIsVisited = False    # 该节点是否被访问过
        
class MyMap(object):
    '''
    成员变量说明：
    self.m_iCapacity    # 图中最对可以容纳的顶点个数
    self.m_iNodeCount   # 已经添加的顶点（结点）个数
    self.m_pNodeArray   # 用来存放顶点数组
    self.m_pMatrix      # 用来存放顶点数组
    '''
    def __init__(self, capacity):
        self.m_iCapacity = capacity    # 图中最对可以容纳的顶点个数
        self.m_iNodeCount = 0          # 已经添加的顶点（结点）个数
        self.m_pMatrix = [0]*(self.m_iCapacity**2)    # 用来存放邻接矩阵（一维数组），None可改为0
        self.m_pNodeArray = []*self.m_iCapacity     # 用来存放顶点数组
        for i in range(self.m_iCapacity):
            self.m_pNodeArray.append(Node())
        
    def __del__(self):
        del self.m_pNodeArray
        del self.m_pMatrix
        
    def addNode(self, pNode):
        '''向图中添加顶点（结点）'''
        if pNode is None:
            return False
        self.m_pNodeArray[self.m_iNodeCount].m_cData = pNode.m_cData
        self.m_iNodeCount += 1
        return True
    
    def resetNode(self):
        '''重置结点，将结点置成未访问的状态'''
        for i in range(self.m_iNodeCount):
            self.m_pNodeArray[i].m_bIsVisited = False
            
    def setValueToMatrixForDirectedGraph(self, row, col, val=1):
        '''为有向图设置邻接矩阵'''
        if row < 0 and row >= self.m_iCapacity:
            return False
        
        if col < 0 and col >= self.m_iCapacity:
            return False
        
        self.m_pMatrix[row*self.m_iCapacity+col] = val
        return True
        
    def setValueToMatrixForUndirectedGraph(self, row, col, val=1):
        '''为无向图设置邻接矩阵'''
        if row < 0 and row >= self.m_iCapacity:
            return False
        
        if col < 0 and col >= self.m_iCapacity:
            return False
        
        # 因为上三角与下三角一样，所以要设置两个
        self.m_pMatrix[row*self.m_iCapacity+col] = val
        self.m_pMatrix[col*self.m_iCapacity+row] = val
        return True
    
    def getValueFromMatrix(self, row, col):
        '''从矩阵中获取权值'''
        if row < 0 and row >= self.m_iCapacity:
            return False
        
        if col < 0 and col >= self.m_iCapacity:
            return False
        
        return self.m_pMatrix[row*self.m_iCapacity+col]
    
    def printMatrix(self):
        '''打印邻接矩阵'''
        for i in range(self.m_iCapacity):
            tmp = []
            for k in range(self.m_iCapacity):
                tmp.append(self.m_pMatrix[i*self.m_iCapacity+k])
            print ' '.join(map(str,tmp))
        # 上面等同于下面一行
        # print '\n'.join([' '.join([str(self.m_pMatrix[i*self.m_iCapacity+k]) for k in range(self.m_iCapacity)]) for i in range(self.m_iCapacity)])
    
    def depthFirstTraverse(self, nodeIndex):
        '''深度优先遍历'''
        print self.m_pNodeArray[nodeIndex].m_cData
        self.m_pNodeArray[nodeIndex].m_bIsVisited = True
        
        for i in range(self.m_iCapacity):
            value = self.getValueFromMatrix(nodeIndex, i)
            if value == 1:
                if self.m_pNodeArray[i].m_bIsVisited:
                    continue
                else:
                    self.depthFirstTraverse(i)
            else:
                continue
        
    def breadthFirstTraverse(self, nodeIndex):
        '''广度优先遍历'''
        print self.m_pNodeArray[nodeIndex].m_cData
        self.m_pNodeArray[nodeIndex].m_bIsVisited = True
        
        curVec = [] # 保存当前层的节点的索引
        curVec.append(nodeIndex)
        
        self.__breadthFirstTraverseImpl(curVec)
    
    def __breadthFirstTraverseImpl(self, preVec):
        '''广度优先遍历实现函数
        preVec 保存的上层的节点
        '''
        value = 0
        curVec = [] # 保存当前层的节点的索引
        for j in range(len(preVec)):
            for i in range(self.m_iCapacity):
                value = self.getValueFromMatrix(preVec[j], i)
                if value == 1:
                    if self.m_pNodeArray[i].m_bIsVisited:
                        continue
                    else:
                        print self.m_pNodeArray[i].m_cData
                        self.m_pNodeArray[i].m_bIsVisited = True
                        curVec.append(i)
                        
        if len(curVec) == 0:
            return 
        else:
            self.__breadthFirstTraverseImpl(curVec)
    
    
if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    pMap = MyMap(len(nodes))
    
    for i in nodes:
        pNode = Node(i)
        pMap.addNode(pNode)
        
    pMap.setValueToMatrixForUndirectedGraph(0, 1)
    pMap.setValueToMatrixForUndirectedGraph(0, 3)
    pMap.setValueToMatrixForUndirectedGraph(1, 2)
    pMap.setValueToMatrixForUndirectedGraph(1, 5)
    pMap.setValueToMatrixForUndirectedGraph(3, 6)
    pMap.setValueToMatrixForUndirectedGraph(3, 7)
    pMap.setValueToMatrixForUndirectedGraph(6, 7)
    pMap.setValueToMatrixForUndirectedGraph(2, 4)
    pMap.setValueToMatrixForUndirectedGraph(4, 5)
    
    print '-----print matrix-------'
    pMap.printMatrix()
    
    print '------depth first-------'
    pMap.depthFirstTraverse(0)
    pMap.resetNode()
    
    print '------breadth first-----'
    pMap.breadthFirstTraverse(0)
    pMap.resetNode()