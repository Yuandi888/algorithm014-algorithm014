学习笔记

[TOC]

# Python 递归代码模版

```python
def recursion(level, param1, param2, ...):
  # recursion terminator
  if level > MAX_LEVEL:
    process_result
    return
  
  # process logic in current level
  process(level, data...)
  
  # drill down
  self.recursion(level + 1, p1, ...)
  
  # reverse the current level status if needed
```

# 堆 Heap

Heap：可以迅速找到一堆数中的最大或者最小值的数据结构。

将根节点最大的堆叫做大顶堆或大根堆，根节点最小的堆叫做小顶堆或小根堆。
常见的堆有二叉堆、斐波那契堆等。

假设是大顶堆，常见操作的时间复杂度：

Find-max:		  O(1)
Delete-max:	  O(logN)
Insert(create):	O(logN) or O(1)



## 二叉堆性质

通过完全二叉树来实现（注意：不是二叉搜索树）；

二叉堆（大顶）满足下列性质：
1、是一棵完全树
2、树中任意节点的值总是 >= 其子节点的值；



## 二叉堆的实现细节

1、二叉堆一般通过“数组”来实现

2、假设“第一个元素”在数组中的索引为0的话，父节点喝子节点的位置关系如下：
	(1) 索引为i的左孩子的索引是(2 * i + 1)
	(2) 索引为i的右孩子的索引是(2 * i + 2)
	(3) 索引为i的父节点的索引是floor((i - 1) / 2)

### Insert 插入操作 - 时间复杂度：O(logN)

1、新元素一律先插入到堆的尾部
2、依次向上调整整个堆的结构（一直到根即可）
HeapifyUp

### Delete Max 删除堆顶操作 - 时间复杂度：O(logN)

1、将堆顶元素去掉，将堆尾元素放在顶部位置
2、依次从根部向下调整整个堆的结构（一直到堆尾即可）
HeapifyDown



# 图

Graph(V, E)

V - vertex：点
1、度 -- 入度、出度
2、点与点之间：连通与否

E -- edge：边
1、有向喝无向
2、权重



## 图的表示和分类

图也可以用矩阵来表示（Adjacency matrix）也可以用列表来表示（Adjacency list）

无向无权图
有向无权图
无向有权图



# 分治 Divide & Conquer

分治代码模版

```python
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
    print_result
    return
  # prepare data
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)
  # conquer subproblems
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)
  ...
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3, ...)
  
  # revert the current level states
```



# 回溯

回溯采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其他的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

1、找到一个可能存在的正确的答案；

2、在尝试了所有可能的分步方法后宣布该问题没有答案。

在最坏的情况下，回溯法会导致一次复杂度为**<u>指数时间</u>**的计算