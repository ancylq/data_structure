# coding:utf-8
'''
同时满足下面条件的树即为二叉堆：
1. 完全二叉树
2. 子节点均不大于（或小于）其父节点称为最大堆（或最小堆）

将n个元素诸葛插入到一个空堆中，算法复杂度为O(nlogn)
heapify的过程，算法复杂度为O(n)
'''
class MyMaxHeap(object):
    '''
    以最大堆为例，索引从0开始
                            62 (1)
                  /                    \
                41 (2)                  30(3)
          /            \            /         \
         28 (4)         16 (5)     22 (6)      13 (7)
     /      \          /
    19 (8)  17 (9)    15 (10)
    存储：[-, 62, 41, 30, 28, 16, 22, 13, 19, 17, 15]
    '''
    
    def __init__(self, capacity):
        self.data = [None] * (capacity + 1) # 第0索引空出来
        self.count = 0
        self.capacity = capacity
        
    def __del__(self):
        del self.data
        
    def _shifUp(self, k):
        '''大节点上移
        判断当前节点的值是否大于其父节点，若大于，则与父节点交换值，
        直至遇到比当前节点大的，或是到达根节点
        '''
        while (k > 1 and self.data[k/2] < self.data[k]): 
            self.data[k/2], self.data[k] = self.data[k], self.data[k/2]
            k /= 2
            
    def _shifDown(self, k):
        '''根节点下移（用于取最大元素后）
        将该节点与该节点的孩子节点中值较大者的那个交换值
        然后再继续向下比较移动，直到合适的位置
        '''
        while (2*k <= self.count):  # 节点有左孩子就代表该节点一定有孩子
            j = 2*k
            if j+1 <= self.count and self.data[j+1]>self.data[j]:
                j += 1
            
            if self.data[k] >= self.data[j]:
                break
            
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j
    
    def insert(self, item):
        '''插入节点
        只能插入叶子节点
        插入后，调整各个节点位置，保证最大堆
        '''
        assert(self.count+1<=self.capacity)
        self.data[self.count+1] = item # 第0个索引不存
        self.count += 1
        self._shifUp(self.count)
    
    def getMax(self):
        '''取最大值
        最大堆的取值只能取根节点，也即为取最大值。
        1. 第一个值即为最大值
        2. 交换最后一个叶子节点与第一个节点的值，使最后一个叶子节点成为新的根节点
        3. 将新的根节点向下移动到合适的位置
        '''
        assert(self.count > 0)
        result = self.data[1] # 第0个索引不存
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        del self.data[self.count]
        self.count -= 1
        self._shifDown(1)
        return result
    
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
if __name__ == '__main__':
    import random
    old = random.shuffle(range(3))
    maxheap = MyMaxHeap(3)
    for i in old:
        maxheap.insert(i)
        
    for i in range(3):
        print maxheap.getMax()