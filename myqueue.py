# coding:utf-8

class MyQueue(object):

    def __init__(self, queueCapacity):
        self.m_iQueueCapacity = queueCapacity
        self.m_pQueue = [None]*queueCapacity
        self.ClearQueue()


    def __del__(self):
        self.m_pQueue = None

    def ClearQueue(self):
        self.m_iHead = 0
        self.m_iTail = 0
        self.m_iQueueLen = 0

    @property
    def QueueEmpty(self):
        return True if self.m_iQueueLen == 0 else False

    @property
    def QueueFull(self):
        return True if self.m_iQueueLen == self.m_iQueueCapacity else False

    @property
    def QueueLen(self):
        return self.m_iQueueLen

    def EnQueue(self, element):
        if self.QueueFull:
            return False

        self.m_pQueue[self.m_iTail] = element
        self.m_iTail += 1
        # 当m_iTail指向尾后，执行过加1操作后会超出范围，所以进行取余，使其指向起始位置
        self.m_iTail = self.m_iTail % self.m_iQueueCapacity
        self.m_iQueueLen += 1
        return True

    def DeQueue(self):
        if self.QueueEmpty:
            return False

        element = self.m_pQueue[self.m_iHead]
        self.m_iHead += 1
        self.m_iHead = self.m_iHead % self.m_iQueueCapacity
        self.m_iQueueLen -= 1
        return element

    def QueueTraverse(self):
        for i in range(self.m_iHead, self.m_iHead+self.m_iQueueLen):
            print '前面还有%d个数' % (i-self.m_iHead)
            print self.m_pQueue[i%self.m_iQueueCapacity]


def main():
    p = MyQueue(4)
    p.EnQueue(10)
    p.EnQueue(12)
    p.EnQueue(15)
    p.EnQueue(18)
    p.EnQueue(20)
    p.QueueTraverse()

    print '-----delete element------'
    print p.DeQueue()
    print p.DeQueue()
    
    print '-----traverse again-----'
    p.QueueTraverse()

    print '-----clear and traverse----'
    p.ClearQueue()
    p.QueueTraverse()

    print 'insert again-------'
    p.EnQueue(30)
    p.EnQueue(40)
    p.QueueTraverse()
main()
