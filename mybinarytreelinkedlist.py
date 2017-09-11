# coding:utf-8
'''
二叉树链表
'''
class Node(object):
    __slots__ = ('index', 'data', 'pLChild', 'pRChild', 'pParent')

    def __init__(self):
        '''
        初始化时，根节点的数据域无意义。
        '''
        self.index = 0
        self.data = 0
        self.pLChild, self.pRChild, self.pParent = None, None, None
        
    def searchNode(self, nodeIndex):
        if self.index == nodeIndex:
            return self

        if self.pLChild is not None:
            if self.pLChild.index == nodeIndex:
                return self.pLChild
            else:
                temp = self.pLChild.searchNode(nodeIndex)
                if temp is not None:
                    return temp
            
        if self.pRChild is not None:
            if self.pRChild.index == nodeIndex:
                return self.pRChild
            else:
                # 右边已经找过，左边可以直接返回值，也可参照右边的返回
                return self.pRChild.searchNode(nodeIndex)

        return None

    def deleteNode(self):
        if self.pLChild is not None:
            self.pLChild.deleteNode()
        if self.pRChild is not None:
            self.pRChild.deleteNode()
        if self.pParent is not None:
            if self.pParent.pLChild == self:
                self.pParent.pLChild = None
            if self.pParent.pRChild == self:
                self.pParent.pRChild = None
        del self
        
    def preorderTraversal(self):
        '''前序遍历'''
        print str(self.index)+'------'+str(self.data)
        
        if self.pLChild is not None:
            self.pLChild.preorderTraversal()
            
        if self.pRChild is not None:
            self.pRChild.preorderTraversal()
            
    def inorderTraversal(self):
        '''中序遍历'''
        if self.pLChild is not None:
            self.pLChild.inorderTraversal()
            
        print str(self.index)+'------'+str(self.data)
        
        if self.pRChild is not None:
            self.pRChild.inorderTraversal()
            
    def postorderTraversal(self):
        '''后序遍历'''
        if self.pLChild is not None:
            self.pLChild.postorderTraversal()
        
        if self.pRChild is not None:
            self.pRChild.postorderTraversal()
        
        print str(self.index)+'------'+str(self.data)

class MyBinaryTreeLinkedList(object):
    def __init__(self):
        self.m_pRoot = Node()

    def __del__(self):
        '''
        只要删除根结点，则整个树都删除了
        '''
        # self.m_pRoot.deleteNode() # 与下面二选一
        self.deleteNode(0)

    def searchNode(self, nodeIndex):
        return self.m_pRoot.searchNode(nodeIndex)

    def addNode(self, nodeIndex, direction, pNode):
        temp = self.searchNode(nodeIndex) 
#         print temp
#         print pNode
        if not temp:
            return False
        
        # 为防止pNode被修改，所以要重新付给新的节点
        node = Node()
        if not node:
            return False
        node.index = pNode.index
        node.data = pNode.data
        node.pParent = temp
        
        if direction == 0:
            # 挂在左边
            temp.pLChild = node
        else:
            # 挂在右边
            temp.pRChild = node
        return True

    def deleteNode(self, nodeIndex):
        '''
        节点下对应的子节点，以及子节点的子节点都要删除
        '''
        temp = self.searchNode(nodeIndex) 
        if not temp:
            return False
        
#         if pNode is not None:
#             pNode.data = temp.data
            
        temp.deleteNode()
        return True

    def preorderTraversal(self):
        '''前序遍历'''
        self.m_pRoot.preorderTraversal()

    def inorderTraversal(self):
        '''中序遍历'''
        self.m_pRoot.inorderTraversal()

    def postorderTraversal(self):
        '''后序遍历'''
        self.m_pRoot.postorderTraversal()

if __name__ == '__main__':
    node1 = Node()
    node1.index = 1
    node1.data = 5
    
    node2 = Node()
    node2.index = 2
    node2.data = 8
    
    node3 = Node()
    node3.index = 3
    node3.data = 2
    
    node4 = Node()
    node4.index = 4
    node4.data = 6
    
    node5 = Node()
    node5.index = 5
    node5.data = 9
    
    node6 = Node()
    node6.index = 6
    node6.data = 7
    
    tree = MyBinaryTreeLinkedList() # 实例化后，根节点默认创建
    
    # data(index)
    #         0(0)
    #    5(1)      8(2)
    # 2(3) 6(4) 9(5) 7(6)
    
    tree.addNode(0, 0, node1)
    tree.addNode(0, 1, node2)
    
    tree.addNode(1, 0, node3)
    tree.addNode(1, 1, node4)
                  
    tree.addNode(2, 0, node5)
    tree.addNode(2, 1, node6)
    
    print '----- preorder traversal -----'
    tree.preorderTraversal() # 0134256
    
    print '----- inorder traversal -----'
    tree.inorderTraversal() # 3140526
    
    print '----- postorder traversal -----'
    tree.postorderTraversal() # 3415620
     
    tree.deleteNode(6)
    tree.deleteNode(2)
