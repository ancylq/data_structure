# coding:utf-8
import mymap
'''
        A
    /   |   \
  6/   1|    \5
  /     |     \
B --2-- F --9-- E    
  \    / \     /
  3\  /8  \4  /2
    C --7-- D
    
Kruskal算法分析（以上图为例）：
1. 取出所有边
2. 从所有边中取出最小生成树的边
   1）找到算法结束的条件
   2）从边集合中找到最小边
   3）找出最小边连接的点
   4）找出点所在的点集合
   5）根据所在点集合的不同做出不同处理
例如：
从A点开始，取最小边A-F，顶点集合变为[A,F]
再取剩下最小边B-F，顶点集合变为[A,F,B]
再取剩下最小边D-E，顶点集合变为[A,F,B]和[D,E]
再取剩下最小边B-C，顶点集合变为[A,F,B,C]和[D,E]
再取剩下最小边F-D，顶点集合变为[A,F,B,C,D,E]，
直到有边将所有的顶点集合串联起来，结束
'''
class Edge(object):
    def __init__(self, nodeIndexA=0, nodeIndexB=0, weightValue=0):
        self.m_iNodeIndexA = nodeIndexA
        self.m_iNodeIndexB = nodeIndexB
        self.m_iWeightValue = weightValue
        self.m_bSelected = False
        
class MyKruskal(mymap.MyMap):
    def __init__(self, capacity):
        super(MyKruskal, self).__init__(capacity)
        self.m_pEdge = []  # 存最小生成树的边，边数=顶点数-1
        for i in range(self.m_iCapacity-1):
            self.m_pEdge.append(Edge())
    
    def __del__(self):
        super(MyKruskal, self).__del__()
        del self.m_pEdge
        
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
    
    def kurskalTree(self):
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
    pMap = MyKruskal(len(nodes))
    
    for node in nodes:
        pNode = mymap.Node(node)
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
    pMap.kurskalTree() 
    # 执行结果：
#     0 --> 5 : 1
#     1 --> 5 : 2
#     3 --> 4 : 2
#     1 --> 2 : 3
#     3 --> 5 : 4
