# data_structure
数据结构

## 队列
一种特殊的线性表，它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作。
进行插入操作的端称为队尾，进行删除操作的端称为队头。<br>
队列是按照“先进先出”或“后进后出”的原则组织数据的。队列中没有元素时，称为空队列。

### myqueue.py
环形队列的实现<br>
当入队元素个数大于队列的容量，多余元素入队失败。<br>
入队个数与队列容量取余来确定下一个元素要插入的位置索引。 <br>

## 栈
是只能在某一端插入和删除的特殊线性表。<br>
它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶。<br>
需要读数据的时候从栈顶开始弹出数据（最后一个数据被第一个读出来）。<br>

### mystack.py
栈的实现<br>

## 链表
是一种物理存储单元上非连续、非顺序的存储结构，它既可以表示线性结构，也可以用于表示非线性结构，
数据元素的逻辑顺序是通过链表中的指针链接次序实现的。<br>
链表由一系列结点（链表中每一个元素称为结点）组成，结点可以在运行时动态生成。<br>
每个结点包括两个部分：一个是存储数据元素的数据域，另一个是存储下一个结点地址的指针域。<br>

### mysequentialList.py
顺序表的实现<br>
使用数组来存储，通过数组的索引来取元素的前驱和后继<br>

### mysinglyLinkedList.py
单向链表的实现<br>
每个节点为一个对象，该对象包含两个部分：一个是存储数据元素的数据域，另一个是存储下一个结点地址的指针域。<br>
初始化时，第一个节点的数据域无用，指针域指向空。<br>

## 树
树是节点的有限集合。<br>
节点的度是节点孩子的个数。<br>
节点的深度即节点所在的层数。<br>
索引从0开始，父节点表示为i/2，则i*2+1为左孩子，i*2+2为右孩子，最后一个非叶子节点的索引为：叶子个数/2。<br>
索引从1开始，父节点表示为(i+1)/2，则i*2为左孩子，i*2+1为右孩子，最后一个非叶子节点的索引为：(叶子个数-1)/2。<br>

### mybinarytreearray.py
二叉树数组的实现<br>
用数组存储二叉树，按照广度存储。<br>

### mybinarytreelinkedlist.py
二叉树链表的实现<br>
每个节点为一个对象，该对象包含五部分：当前索引，当前数据，左孩子指针，右孩子指针，父节点指针<br>

## 图
图是由结点的有穷集合V和边的集合E组成。<br>
其中，为了与树形结构加以区别，在图结构中常常将结点称为顶点，边是顶点的有序偶对，
若两个顶点之间存在一条边，就表示这两个顶点具有相邻关系。<br>

### mymap.py
图的存储（邻接矩阵）与图的遍历（深度优先、广度优先）的实现。<br>
图分为有向图、无向图。<br>
无向图的上三角和下三角堆成，在生成邻接矩阵时要两个地方同时赋值。<br>
以无向图为例：<br>
例：<br>
&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;B&nbsp;C&nbsp;D&nbsp;E&nbsp;F&nbsp;G&nbsp;H
&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;\\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;1,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,
&nbsp;&nbsp;B&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,
&nbsp;/&nbsp;\\&nbsp;&nbsp;/&nbsp;\\&nbsp;&nbsp;&nbsp;&nbsp;==>&nbsp;&nbsp;C&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==>&nbsp;&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;0,
C&nbsp;&nbsp;&nbsp;F&nbsp;G--H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;1,
&nbsp;\\&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,
&nbsp;&nbsp;E&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;0,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;1,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0]

### myprim.py
prim的实现----最小生成树<br>
例：<br>
        A<br>
    /   |   \<br>
  6/   1|    \5<br>
  /     |     \<br>
B --2-- F --9-- E    <br>
  \    / \     /<br>
  3\  /8  \4  /2<br>
    C --7-- D<br>
    <br>
Prim算法分析（以上图为例）：<br>
1. 以点集合[A]为起点，从待选边集合[A-B(6), A-F(1), A-E(5)]中选取权之最小的边A-F(1)放入到<br>
   边集合中[A-F]，同时将F放入到点集合中[A,F]<br>
2. 然后再以F为起点，从待选边集合[A-B(6), A-E(5), F-B(2), F-C(8), F-D(4), F-E(9)]中选取<br>
   权值最小的边F-B(2)放入到边集合中[A-F, F-B]，同时将B点放到点集合中[A, F, B]<br>
3. 以此类推，直到所有点放到点集合中，边集合个数=点集合个数-1<br>

### mykruskal.py
kruskal的实现----最小生成树<br>
<br>
Kruskal算法分析（以上面prim的图为例）：<br>
1. 取出所有边<br>
2. 从所有边中取出最小生成树的边<br>
   1）找到算法结束的条件<br>
   2）从边集合中找到最小边<br>
   3）找出最小边连接的点<br>
   4）找出点所在的点集合<br>
   5）根据所在点集合的不同做出不同处理<br>
例如：<br>
从A点开始，取最小边A-F，顶点集合变为[A,F]<br>
再取剩下最小边B-F，顶点集合变为[A,F,B]<br>
再取剩下最小边D-E，顶点集合变为[A,F,B]和[D,E]<br>
再取剩下最小边B-C，顶点集合变为[A,F,B,C]和[D,E]<br>
再取剩下最小边F-D，顶点集合变为[A,F,B,C,D,E]，<br>
直到有边将所有的顶点集合串联起来，结束<br>

### myallmap.py
整合了图的存储、图的深度遍历、Prim最小生成树、Kruskal最小生成树<br>

## 堆
在计算机科学中，堆是一种特殊的树形数据结构，每个结点都有一个值。<br>
通常我们所说的堆的数据结构，是指二叉堆。堆的特点是根结点的值最小（或最大），且根结点的两个子树也是一个堆。<br>
同时满足下面条件的树即为二叉堆：<br>
1. 完全二叉树<br>
2. 子节点均不大于（或小于）其父节点称为最大堆（或最小堆）<br>

### mymaxheap.py
最大堆的实现<br>
大节点上移 shifUp<br>
    判断当前节点的值是否大于其父节点，若大于，则与父节点交换值，<br>
    直至遇到比当前节点大的，或是到达根节点<br>
根节点下移（用于取最大元素后）shifDown<br>
    将该节点与该节点的孩子节点中值较大者的那个交换值<br>
    然后再继续向下比较移动，直到合适的位置<br>
取最大值<br>
    最大堆的取值只能取根节点，也即为取最大值。<br>
    1. 第一个值即为最大值<br>
    2. 交换最后一个叶子节点与第一个节点的值，使最后一个叶子节点成为新的根节点<br>
    3. 将新的根节点向下移动到合适的位置<br>
    
### myheapify.py
将一个数组整理成最大堆(或最小堆)，称为heapify<br>
整理过程（以最大堆为例）：<br>
    1 找到第一个非叶子节点的索引<br>
    2 依次将最后一个非叶子节点的索引到根节点索引所对应的树利用shifDown将其组成最大堆<br>
