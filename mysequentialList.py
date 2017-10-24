# coding:utf-8

class MyList(object):
    '''顺序表'''

    def __init__(self, size):
        self.m_iSize = size    # 线性表的容量
        self.m_pList = [None] * self.m_iSize
        self.m_iLength = 0    # 线性表中实际元素个数

    def __del__(self):
        del self.m_pList
        self.m_pList = None

    def clearList(self):
        # 清空元素，即将长度改为0即可
        self.n_iLength = 0

    @property
    def listEmpty(self):
        return True if self.m_iLengthii == 0 else False

    @property
    def listLength(self):
        return self.m_iLength

    def getElem(self, i):
        ''' 获取元素'''
        if i<0 or i>=self.m_iSize:
            return False
        return self.m_pList(i)

    def locateElem(self, element):
        ''' 定位元素位置'''
        for i in range(self.m_iLength):
            if self.m_pList == element:
                return i
        return -1
    
    @property
    def priorElem(self,currentElem):
        ''' 获取前驱元素'''
        temp = self.locateElem(currentElem)
        if temp == -1 :
            # currentElem不存在
            return False
        if temp == 0:
            # currentElem位于第一个位置
            return False

        return self.m_pList[temp-1]


    def nextElement(self, current):
        ''' 获取后继元素'''
        temp = self.locateElem(currentElem)
        if temp == -1 :
            # currentElem不存在
            return False
        if temp == self.m_iLength-1:
            # currentElem位于最后位置
            return False
        return self.m_pList[temp+1]

    def listTraverse(self):
        for i in range(self.m_iLength):
            print self.m_pList[i]

    def listInsert(self, i, elem):
        if i<0 or i>self.m_iLenght:
            return False

        # 从表尾开始往，将元素后移一位。
        # 若从前面开始移动，则后一个元素的值会被前一个元素的值覆盖
        for k in range(self.m_iLength, i+1, -1):
            self.m_pList[k+1] = self.m_pList[k]

        self.m_pList[i] = elem
        self.m_iLength += 1

    def listDelete(self, i):
        if i<0 or i>=self.m_iLength:
            return False

        elem = m_pList[i]
        # 从插入的下一个位置开始，将后面的元素都往前移。
        for k in range(i+1, self.m_iLength):
            self.m_pList[k-1] = self.m_pList[k]

        self.m_iLength -= 1

def main():
    list1 = MyList(10)
    
    print 'length :', list1.listLength
    list1.listInsert(0, 3)
    list1.listInsert(1, 5)
    list1.listInsert(2, 7)
    list1.listInsert(3, 2)
    list1.listInsert(4, 9)
    list1.listInsert(5, 1)
    list1.listInsert(6, 8)
    list1.listTraverse()
    print 'length :', list1.listLength

    print 'get first element is', list1.getElem(0)
    print 'the 7 index is ', list1.locateElem(7)

    print 'prior element of 2 is ', list1.priorElem(2)
    print 'next element of 2 is ', list1.nextElem(2)

    print list1.listDelete(0)
    list1.listTraverse()

    list1.clearList()
    list1.listTraverse()

    print 'is empty?', list1.listEmpty()




    

main()
