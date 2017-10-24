# coding:utf-8
'''
将一个数组整理成最大堆(或最小堆)，称为heapify

整理过程（以最大堆为例）：
1 找到第一个非叶子节点的索引
2 依次将最后一个非叶子节点的索引到根节点索引所对应的树利用shifDown将其组成最大堆

注：对于完全二叉树(索引从1开始）
最后一个非叶子节点的索引为：叶子个数/2

shifDown：根节点下移
    将该节点与该节点的孩子节点中值较大者的那个交换值
    然后再继续向下比较移动，直到合适的位置
    
将n个元素诸葛插入到一个空堆中，算法复杂度为O(nlogn)
heapify的过程，算法复杂度为O(n)
'''
class MyHeapify(object):
    def __init__(self, arr):
        self.date = [None] + arr  # 第0个位置不存
        self.capacity = len(arr)
        self.count = len(arr)
        
        for i in range(self.count/2, 0, -1):  # 0索引处不存数据，索引不参与heapify
            self._shifDown(i)
    
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

if __name__ == '__main__':
    import random
    
    arr = range(10)
    random.shuffle(arr)
    hps = HeapifySort(arr)
    for i in arr:
        print hps.getMax()
