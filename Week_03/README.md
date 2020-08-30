学习笔记

# （未完）

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

