# coding:utf-8

class MyStack(object):

    def __init__(self, size):
        print 'init---'
        self.m_iSize = size
        self.m_pBuffer = [None]*size
        self.m_iTop = 0 # 栈顶初始值

    def __del__(self):
        del self.m_pBuffer

    @property
    def stackEmpty(self):
        return True if 0 == self.m_iTop else False

    @property
    def stackFull(self):
        return True if self.m_iSize == self.m_iTop else False

    def clearStack(self):
        # 不用真的清空，只要确保栈顶为0，其他值可以重新覆盖
        self.m_iTop = 0
    
    @property
    def stackLength(self):
        return self.m_iTop


    def push(self, element):
        if self.stackFull:
            return False # 可以使用raise

        self.m_pBuffer[self.m_iTop] = element
        self.m_iTop += 1 # 始终指向下一个可以插入值的位置
        return True

    def pop(self):
        if self.stackEmpty:
            return False

        self.m_iTop -= 1
        element = self.m_pBuffer[self.m_iTop]
        return element

    def stackTraverse(self, isFromButtom=True):
        print 'test'
        if isFromButtom:
            # 从底向上遍历
            for i in range(self.m_iTop):
                print self.m_pBuffer[i]
        else:
            # 从上向下便利
            for i in range(self.m_iTop-1, -1, -1):
                print self.m_pBuffer[i]


def main():
    pStack = MyStack(5)
    
    pStack.push('h')
    pStack.push('e')
    pStack.push('l')
    pStack.push('l')
    pStack.push('o')
    # pStack.push('h')
    print '-----从下向上遍历-----'
    pStack.stackTraverse()
    print '-----从上向下遍历-----'
    pStack.stackTraverse(False)
    
    print '-----弹出顶元素-----'
    print pStack.pop()
    print '-----弹出后遍历（从下到上）-----'
    pStack.stackTraverse()
    print '-----弹出后元素个数-----'
    print pStack.stackLength
    
    print '-----清空栈-----'
    pStack.clearStack()
    
    print '-----清空栈后栈的长度-----'
    print pStack.stackLength

    print 'is Empty?', pStack.stackEmpty
    
    print 'is Full?', pStack.stackFull

main()