# coding: utf-8
'''
图的存储、图的深度遍历、Prim最小生成树、Kruskal最小生成树
'''
class Node(object):
    
    def __init__(self, data=0):
        self.m_cData = data
        self.m_bIsVisited = False    # 该结点是否被访问过

class Edge(object):
    def __init__(self, nodeIndexA=0, nodeIndexB=0, weightValue=0):
        self.m_iNodeIndexA = nodeIndexA
        self.m_iNodeIndexB = nodeIndexB
        self.m_iWeightValue = weightValue
        self.m_bSelected = False
        
class Map(object):
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
            
        self.m_pEdge = []  # 存最小生成树的边，边数=顶点数-1
        for i in range(self.m_iCapacity-1):
            self.m_pEdge.append(Edge())
    
    def __del__(self):
        del self.m_pNodeArray
        del self.m_pMatrix
        del self.m_pEdge
        
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
        
        curVec = [] # 保存当前层的结点的索引
        curVec.append(nodeIndex)
        
        self._breadthFirstTraverseImpl(curVec)
    
    def _breadthFirstTraverseImpl(self, preVec):
        '''广度优先遍历实现函数
        preVec 保存的上层的结点
        '''
        value = 0
        curVec = [] # 保存当前层的结点的索引
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
            self._breadthFirstTraverseImpl(curVec)
        
    def _isInSet(self, nodeSet, target):
        for i in range(len(nodeSet)):
            if nodeSet[i] ==  target:
                return True
        return False
    
    def _getMinEdge(self, edgeVec):
        '''
        参数说明：
        edgeVec   Edge()类型的参数的列表
        '''
        minWeight = 0
        edgeIndex = 0
        
        # 取第一条没访问过的边
        for i in range(len(edgeVec)):
            if not edgeVec[i].m_bSelected:
                minWeight = edgeVec[i].m_iWeightValue
                edgeIndex = i
                break
            
        if minWeight == 0:
            # 意味着edgVec中所有边都访问过
            return -1
        
        # 从剩下的边中取最小的权值
        for i in range(edgeIndex, len(edgeVec)):
            if not edgeVec[i].m_bSelected:
                if minWeight > edgeVec[i].m_iWeightValue:
                    minWeight = edgeVec[i].m_iWeightValue
                    edgeIndex = i
        return edgeIndex
    
    def primTree(self, nodeIndex):
        '''Prim最小生成树'''
        edgeCount = 0    # 计算边数
        nodeVec = []    # 存储点的索引
        edgeVec = []    # 所有点链接的边(待选边)
        
        nodeVec.append(nodeIndex)
        self.m_pNodeArray[nodeIndex].m_bIsVisited = True
        
        print '-----find nodexIndex---', self.m_pNodeArray[nodeIndex].m_cData
#         nodeVec.append(nodeIndex)
        # 算法结束条件
        while (edgeCount != self.m_iCapacity-1):
            temp = nodeVec[-1]
            
            for i in range(self.m_iCapacity):
                value = self.getValueFromMatrix(temp, i)
                if value != 0:
                    if self.m_pNodeArray[i].m_bIsVisited:
                        continue
                    else:
                        edge = Edge(temp, i, value)
                        edgeVec.append(edge)
                        
            # 从待选边集合中找出最小的边
            edgeIndex = self._getMinEdge(edgeVec)
            edgeVec[edgeIndex].m_bSelected = True
            print '----finded edge----'
            print edgeVec[edgeIndex].m_iNodeIndexA,'-->',edgeVec[edgeIndex].m_iNodeIndexB, ':', edgeVec[edgeIndex].m_iWeightValue
            
            # 将选中的边放入到边集合中
            self.m_pEdge[edgeCount] = edgeVec[edgeIndex] 
            edgeCount += 1
            
            nextNodeIndex = edgeVec[edgeIndex].m_iNodeIndexB
            nodeVec.append(nextNodeIndex)
            self.m_pNodeArray[nextNodeIndex].m_bIsVisited = True
            
            print '----finded nextNodeIndex----',self.m_pNodeArray[nextNodeIndex].m_cData
    
    def kruskalTree(self):
        '''Kruskal最小生成树'''
        value = 0
        edgeCount = 0
        nodeSets = [[]] # 存放结点集合
        edgeVec = [] # 存放边的集合
        
        # 1 取出所有边
        # 取邻接矩阵上三角的值即可，不包括主对角线
        for i in range(self.m_iCapacity):
            for k in range(i+1, self.m_iCapacity):
                value = self.getValueFromMatrix(i, k)
                if value != 0:
                    edge = Edge(i, k, value)
                    edgeVec.append(edge)
        
        # 2 从所有边中取出组成最小生成树的边
        # 1）算法结束条件
        while (edgeCount < self.m_iCapacity-1):
            # 2) 从边集合中找到最小边
            minEdgeIndex = self._getMinEdge(edgeVec)
            edgeVec[minEdgeIndex].m_bSelected = True
            
            # 3) 找出最小边连接的点
            nodeAIndex = edgeVec[minEdgeIndex].m_iNodeIndexA
            nodeBIndex = edgeVec[minEdgeIndex].m_iNodeIndexB
            
            nodeAInSetLabel, nodeBInSetLabel =  -1, -1 # 点所在的集合索引
            
            # 4) 找出点所在的点集合
            # 先判断A
            for i in range(len(nodeSets)):
                nodeAIsInSet = self._isInSet(nodeSets[i], nodeAIndex)
                # 不可能有一个顶点在两个顶点集合中
                if nodeAIsInSet:
                    nodeAInSetLabel = i
                    
            # 再判断B
            for i in range(len(nodeSets)):
                nodeBIsInSet = self._isInSet(nodeSets[i], nodeBIndex)
                if nodeBIsInSet:
                    nodeBInSetLabel = i
                    
            # 5) 根据点所在的集合的不同做出不同处理
            if nodeAInSetLabel == -1 and nodeBInSetLabel == -1:
                # A、B都不在集合中，就加到集合中
                vec = []
                vec.append(nodeAIndex)
                vec.append(nodeBIndex)
                nodeSets.append(vec)
                
            elif nodeAInSetLabel == -1 and nodeBInSetLabel != -1:
                # A不在任何一个集合中，就把A加到B所在的集合中
                nodeSets[nodeBInSetLabel].append(nodeAIndex)
                
            elif nodeAInSetLabel != -1 and nodeBInSetLabel == -1:
                # B不在任何一个集合中，就把B加到A所在的集合中
                nodeSets[nodeAInSetLabel].append(nodeBIndex)
                
            elif nodeAInSetLabel != -1 and nodeBInSetLabel != -1 and nodeAInSetLabel != nodeBInSetLabel:
                # A、B分别在不同的集合中
                # 将B结点结合合并到A结点集合中
                nodeSets[nodeAInSetLabel].extend(nodeSets[nodeBInSetLabel])
                # 删除B结点集合,后面的结合前移一位，或是直接 del nodeSets[nodeBInSetLabel]
                for k in range(nodeBInSetLabel, len(nodeSets)-1):
                    nodeSets[k] = nodeSets[k+1]
                    
            elif nodeAInSetLabel != -1 and nodeBInSetLabel != -1 and nodeAInSetLabel == nodeBInSetLabel:
                # A、B在同一个集合中，形成回路
                continue
            
            self.m_pEdge[edgeCount] = edgeVec[minEdgeIndex]
            edgeCount += 1
            
            print edgeVec[minEdgeIndex].m_iNodeIndexA,'-->',edgeVec[minEdgeIndex].m_iNodeIndexB, ':', edgeVec[minEdgeIndex].m_iWeightValue
            
            
if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    pMap = Map(len(nodes))
    
    for node in nodes:
        pNode = Node(node)
        pMap.addNode(pNode)
        
    pMap.setValueToMatrixForUndirectedGraph(0, 1, 6) # A-B 6
    pMap.setValueToMatrixForUndirectedGraph(0, 4, 5) # A-E 5
    pMap.setValueToMatrixForUndirectedGraph(0, 5, 1) # A-F 1
    pMap.setValueToMatrixForUndirectedGraph(1, 2, 3) # B-C 3
    pMap.setValueToMatrixForUndirectedGraph(1, 5, 2) # B-F 2
    pMap.setValueToMatrixForUndirectedGraph(2, 5, 8) # C-F 8
    pMap.setValueToMatrixForUndirectedGraph(2, 3, 7) # C-D 7
    pMap.setValueToMatrixForUndirectedGraph(3, 5, 4) # D-F 4
    pMap.setValueToMatrixForUndirectedGraph(3, 4, 2) # D-E 2
    pMap.setValueToMatrixForUndirectedGraph(4, 5, 9) # E-F 9
    
    pMap.printMatrix()
#     0 6 0 0 5 1
#     6 0 3 0 0 2
#     0 3 0 7 0 8
#     0 0 7 0 2 4
#     5 0 0 2 0 9
#     1 2 8 4 9 0
    pMap.primTree(0)
    # 执行结果：
    # 0-->5:1
    # 5-->1 2
    # 1-->2:3
    # 5-->3:4
    # 3-->4:2
    pMap.kruskalTree() 
    # 执行结果：
#     0 --> 5 : 1
#     1 --> 5 : 2
#     3 --> 4 : 2
#     1 --> 2 : 3
#     3 --> 5 : 4