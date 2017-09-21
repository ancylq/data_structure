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
    
Prim算法分析（以上图为例）：
1. 以点集合[A]为起点，从待选边集合[A-B(6), A-F(1), A-E(5)]中选取权之最小的边A-F(1)放入到
   边集合中[A-F]，同时将F放入到点集合中[A,F]
2. 然后再以F为起点，从待选边集合[A-B(6), A-E(5), F-B(2), F-C(8), F-D(4), F-E(9)]中选取
   权值最小的边F-B(2)放入到边集合中[A-F, F-B]，同时将B点放到点集合中[A, F, B]
3. 以此类推，直到所有点放到点集合中，边集合个数=点集合个数-1
'''
class Edge(object):
    def __init__(self, nodeIndexA=0, nodeIndexB=0, weightValue=0):
        self.m_iNodeIndexA = nodeIndexA
        self.m_iNodeIndexB = nodeIndexB
        self.m_iWeightValue = weightValue
        self.m_bSelected = False

class MyPrim(mymap.MyMap):
    '''Prim（普里姆）最小生成树
    父类成员变量说明：
    self.m_iCapacity    # 图中最对可以容纳的顶点个数
    self.m_iNodeCount   # 已经添加的顶点（结点）个数
    self.m_pNodeArray   # 用来存放顶点数组
    self.m_pMatrix      # 用来存放顶点数组
    '''
    def __init__(self, capacity):
        super(MyPrim, self).__init__(capacity)
        self.m_pEdge = []  # 存最小生成树的边，边数=顶点数-1
        for i in range(self.m_iCapacity-1):
            self.m_pEdge.append(Edge())
        
    def __del__(self):
        super(MyPrim, self).__del__()
        del self.m_pEdge
        
    def primTree(self, nodeIndex):
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

if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    pMap = MyPrim(len(nodes))
    
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
    pMap.primTree(0) 
    # 执行结果：
    # 0-->5:1
    # 5-->1 2
    # 1-->2:3
    # 5-->3:4
    # 3-->4:2