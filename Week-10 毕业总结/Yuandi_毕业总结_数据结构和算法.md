学习笔记

[toc]

# 毕业总结

本课程的主要知识点罗列于此，这是这门课最重要的东西。其他关于如何学习，如何利用时间，如何做题，如何感悟，甚至感动自己等，每个人有每个人的方法和经历，对于一个以结果为导向的时代，过程没有结果重要。另外JensonYao同学做的脑图不错～赞一个！

-----------------------------------

# Week_01

-------------------------



## 过遍数

本质是通过在最合适的时间进行多次训练，达到掌握、熟练和融会贯通知识的作用。



## 计算复杂度

如何计算空间复杂度和时间复杂度，以及常见的时间复杂度的级别：

O(1): Constant Complexity 常数复杂度
O(log n): Logarithmic Complexity 对数复杂度
O(n): Linear Complexity 线性时间复杂度
O(n^2): N square Complexity 平方
O(n^3): N cubic Complexity 立方
O(2^n): Exponential Growth 指数
O(n!): Factorial 阶乘

判断时，只看最高复杂度的运算

比较特别的例子有：
	复杂度：O(logN)
		for(int i=1; i<n; i=i*2){}
和
	复杂度：O(k^n)
		递归，斐波那契数列Fibonacci sequence



## 基础底层逻辑

通过重复来减少工作量，而计算机里最基础的重复包括：

### 循环、判断、递归

一切解题方法都由这三种操作来完成！！！！！！！！！



## 二分查找时间复杂度

各种遍历的时间复杂度都是O(n)，因为每个元素都要过一次。（图遍历、二叉树遍历）

但是二分查找的时间复杂度是O(logN)



## 升维思想+空间换时间

跳表的查询的时间复杂度是O(logN)。利用多级索引进行了升维，也就是用空间换时间！！！！！！！

跳表的元素必须**有序**



## 各种数据结构的复杂度对比：

https://www.bigocheatsheet.com/

值得注意的是哈希表！Hash Table的查询的时间复杂度是O(1)！！！！！！！



## 数组、链表、跳表

数组：在内存中开辟连续的内存地址，存储元素

链表：当前Node对象储存当前节点值与下一节点内存地址

跳表：带有跳表索引的链表，只能用于**元素有序**的情况下，用来取代平衡树二分查找

|          | 左append | 右append | 查询     | 插入     | 删除     |
| -------- | -------- | -------- | -------- | -------- | -------- |
| 数组     | O(1)     | O(1)     | O(1)     | O(n)     | O(n)     |
| 普通链表 | O(1)     | O(1)     | O(n)     | O(1)     | O(1)     |
| 跳表     | O(1)     | O(1)     | O(log n) | O(log n) | O(log n) |

空间复杂度上，数组最少，普通链表第二，跳表最高，但，都是O(n)。

链表应用：LRU Cache

跳表应用：Redis

-----------------------------------

# Week_02

----------------------------------



## 哈希表（Hash table)

其实可以把哈希表理解为带有键值对的字典，从键到值有一个映射函数。

哈希表的查找、插入和删除的平均时间复杂度都是O(1)的，这点很特别也很重要！



## 二叉树的遍历

1.前序（Pre-order）：根-左-右

2.中序（In-order）：左-根-右

3.后序（Post-order）：左-右-根

所谓的“前”、“中”、“后”指的都是根节点的位置，剩余的“左”和“右”都是“先左后右”，或者说是“从左到右”



## 二叉搜索树 Binary Search Tree(BST)

二叉搜索树，也称二叉排序树、有序二叉树(Ordered Binary Tree)、排序二叉树(Sorted Binary Tree)，是指一棵空树或者具有下列性质的二叉 树:

1. 左子树上所有结点的值均小于它的根结点的值;
2. 右子树上所有结点的值均大于它的根结点的值;
3. 以此类推:左、右子树也分别为二叉查找树。 (这就是 重复性!)



需要注意的是二叉搜索树是已经排好序的！所以它的获取、查询、插入和删除的时间复杂度才能为O(log(n))

另外跳表Skip List的最差空间复杂度为O(n log(n))，其余的结构的最差空间复杂度都为O(n)



## 树的遍历

最好用递归！！！！

---------------------------------------

# Week_03

----------------------------------

## 堆 Heap

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

2、假设“第一个元素”在数组中的索引为0的话，父节点和子节点的位置关系如下：
	(1) 索引为i的左孩子的索引是(2 * i + 1)
	(2) 索引为i的右孩子的索引是(2 * i + 2)
	(3) 索引为i的父节点的索引是floor((i - 1) / 2) （索引从0开始，不是从1开始）

### Insert 插入操作 - 时间复杂度：O(logN)

1、新元素一律先插入到堆的尾部
2、依次向上调整整个堆的结构（一直到根即可）
HeapifyUp

### Delete Max 删除堆顶操作 - 时间复杂度：O(logN)

1、将堆顶元素去掉，将堆尾元素放在顶部位置
2、依次从根部向下调整整个堆的结构（一直到堆尾即可）
HeapifyDown

### 注意：二叉堆是堆（优先队列 priority_queue）的一种常见且简单的实现；但是并不是最优的实现。





## 图

Graph(V, E)

V - vertex：点
1、度 -- 入度、出度
2、点与点之间：连通与否

E -- edge：边
1、有向喝无向
2、权重

### 图的表示和分类

图也可以用矩阵来表示（Adjacency matrix）也可以用列表来表示（Adjacency list）

无向无权图
有向无权图
无向有权图

### 基于图的常见算法

#### DFS

```python
visited = set() # 和树中的DFS最大区别
def dfs(node, visited):
	if node in visited: # terminator
		# already visited
		return
	visited.add(node)
  # process current node here.
  ...
  for next_node in node.children():
  	if not next_node in visited: 
      dfs(next_node, visited)
```

#### BFS

```python
def BFS(graph, start, end):
  queue = []
  queue.append([start])
  visited = set() # 和树中的BFS的最大区别
  while queue:
    node = queue.pop() 
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node) 
    queue.push(nodes)
```



## 分治 Divide & Conquer

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



## 回溯

回溯采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其他的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

1、找到一个可能存在的正确的答案；

2、在尝试了所有可能的分步方法后宣布该问题没有答案。

在最坏的情况下，回溯法会导致一次复杂度为**<u>指数时间</u>**的计算

----------------------------------------------------

# Week_04

----------------------------------

## DFS 和 BFS 经验总结

DFS深度优先用递归或栈stack

BFS广度优先用队列queue，先进先出



## DFS代码(Depth-First-Search)

### DFS代码 - 递归写法

``` python
visited = set()

def dfs(node, visited):
  if node in visited: # terminator
    # already visited
    return
  
  visited.add(node)
  
  # process current node here.
  ...
  for next_node in node.children():
    if not next_node in visited:
      dfs(next_node, visited)
```

### DFS代码 - 非递归写法

需要维护一个先进后出的堆 stack

``` python
def DFS(self, tree):
	if tree.root is None:
    return []
  visited, stack = [], [tree.root]
  while stack:
    node = stack.pop()
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node)
    stack.push(nodes)
    
   # other processing word
  ...
```



### BFS 代码(Breadth-First-Search)

需要维护一个先进先出的队列 queue

python实现栈，实现push(),pop(),top(),getMin()方法: https://blog.csdn.net/weixin_38819889/article/details/93591556

``` python
def BFS(graph, start, end):
  queue = []
  queue.append([start])
  visited.add(start)
  
  while queue:
    node = queue.pop() # 其实这里应该是pop(0)，抽出队列中的第一个元素，先进先出。不同与栈stack，DFS用stack
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node)
    queue.push(nodes) # 其实就是list.append(nodes)
```





## 贪心算法 Greedy

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优(即最有利)的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心法可以解决一些最优化问题，如:求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。





## 二分查找



### 二分查找的前提

1、目标函数的单调性（单调递增或递减）

2、存在上下界（bounded）

3、能够通过索引访问（index accessible）



### 二分查找代码模版

``` python
left, right = 0, len(array) - 1
while left <= right:
  mid = (left + right) / 2
  if array[mid] == target:
    # find the target!!
    break or return result
  elif array[mid] < target:
    left = mid + 1
  else:
    right = mid -1`
```

-------------------------

# Week_06

-------------------------------------

## 动态规划

动态规划 和 递归或者分治 没有根本上的区别(关键看有无最优的子结构)

共性:找到重复子问题 

差异性:最优子结构、中途可以淘汰次优解



## 动态规划关键点

1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], ...)

2. 储存中间状态:opt[i]

3. 递推公式(美其名曰:状态转移方程或者 DP 方程)

   Fib: opt[n] = opt[n-1] + opt[n-2]
    二维路径:opt[i,j] = opt\[i+1\][j\] + opt[i\][j+1] (且判断a[i,j]是否空地)



### 最长公共子序列 DP 方程

```
if S1[-1] != S2[-1]: LCS[s1, s2] = Max(LCS[s1-1, s2], LCS[s1, s2-1])

if S1[-1] == S2[-1]: LCS[s1, s2] = LCS[s1-1, s2-1] + 1
```

--------------------------

# Week_07

---------------------------

## 字典树 Trie

自己理解：
字典树是一个多层嵌套的字典，类似于：

```python
Trie = {
        a:{d:{j:k, l:m}
            e:{l:m, n:o}}
        b:{f:{n:o, p:q}
            g:{p:q, r:{o:n}}}
        c:{h:{t:u, v:w, w:t}
            i:{x:{y:z}}}
      }
```

### 基本结构

字典树，即 Trie 树，又称单词查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串(但不仅限于 字符串)，所以经常被搜索引擎系统用于文本词频统计。

它的优点是:最大限度地减少无谓的字符串比较，查询效率比哈希表高。

### 基本性质

1. 结点本身不存完整单词;

2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串;

3. 每个结点的所有子结点路径代表的字符都不相同。

### 核心思想

Trie 树的核心思想是空间换时间。 

利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

```python
class Trie(object):
	def __init__(self):
		self.root = {}
		self.end_of_word = '#'
    
	def insert(self, word):
    node = self.root
    for char in word:
      node = node.setdefault(char, {}) #Trie是多层嵌套的字典，一层层往下钻，有键就返回值，没有键就创建键值对
    node[self.end_of_word] = self.end_of_word #最后一层以'#'收尾
    
  def search(self, word):
    node = self.root
    for char in word:
      if char not in node:
        return False
      node = node[char]
    return self.end_of_word in node
  
  def startsWith(self, prefix):
    node = self.root
    for char in prefix:
      if char not in node:
        return False
      node = node[char]
    return True
```

## 并查集 Disjoint Set

并查集属于比较跳跃式的数据结构，如果不会那就是压根不会，如果一会的话那就会用就行，没有太多可进行发展和自由发挥的空间或非常强的随机应变。这类题目比较死，主要是调用现成的代码，把模版记好之后直接套上去用即可。

判断什么问题可以使用并查集：如有多少个朋友圈，或者它属于谁，或者任意给两个人是不是朋友

### 适用场景

组团、配对问题

Group or not?

### 基本操作

- makeSet(s):建立一个新的并查集，其中包含 s 个单元素集合。
- unionSet(x, y):把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在的集合不相交，如果相交则不合并。
- find(x):找到元素 x 所在的集合的代表，该操作也可以用于判断两个元 素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

### Python实现

```python
def init(p):
  # for i = 0 .. n: p[i] = i;
  p = [i for i in range(n)]
  
def union(self, p, i, j):
  p1 = self.parent(p, i)
  p2 = self.parent(p, j)
  p[p1] = p2
  
def parent(self, p, i):
  root = i
  while p[root] != root:
    root = p[root] #一直往上找到 i 的最顶层的根
  while p[i] != i: # 如果 i 不是最顶层的根。路径压缩？
    x = i; i = p[i]; p[x] = root #将每个节点的父节点都指向root。x = i和p[x] = root表示将x的parent指向root。而i = p[i]表示向上推进一层。
  return root
```



## 第十四课 高级搜索

## 初级搜索

1. 朴素搜索

2. 优化方式:不重复(fibonacci)、剪枝(生成括号问题)

3. 搜索方向:
   DFS: depth first search 深度优先搜索 

   BFS: breadth first search 广度优先搜索

   双向搜索、启发式搜索

### DFS 代码 - 递归写法

```python
visited = set()

def dfs(node, visited):
  if node in visited: # terminator
    # already visited
    return
  
  visited.add(node)
  
  # process current node here.
  ...
  for next_node in  node.children():
    if not next_node in visited:
      dfs(next_node, visited)
```

### DFS 代码 - 非递归写法

```python
def DFS(self, tree):
  if tree.root is None:
    return []
  visited, stack = [], [tree.root] #需要维护一个先进后出的堆
  
  while stack: #DFS和BFS的while循环里代码基本一样，不同是一个是stack一个是queue
    node = stack.pop()
    visited.add(node)
    
    process (node)
    nodes = generate_related_nodes(node)
    stack.push(nodes)
    
	# other processing work
  ...
```

### BFS 代码

```python
def BFS(graph, start, end):
  queue = [] #需要维护一个先进先出的队列
  queue.append([start])
  visited.add(start)
  
  while queue: #DFS和BFS的while循环里代码基本一样，不同是一个是stack一个是queue
    node = queue.pop()
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node)
    queue.push(nodes)
```

#### DFS和BFS的while循环里代码基本一样，不同是一个是stack一个是queue



## 剪枝

### 回溯法

回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当
它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚
至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况:

 • 找到一个可能存在的正确的答案

 • 在尝试了所有可能的分步方法后宣告该问题没有答案 

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

### 八皇后代码

```python
def solveNQueens(self, n):
    if n < 1: return []
    self.result = []
    self.cols = set(); self.pie = set(); self.na = set()
    self.DFS(n, 0, [])
    return self._generate_result(n)

def DFS(self, n, row, cur_state):
    # recursion terminator
    if row >= n:
        self.result.append(cur_state)
        return

    for col in range(n):
        if col in self.cols or row + col in self.pie or row - col in self.na:
          # go die!
            continue
    
    # update the flag
        self.cols.add(col)
        self.pie.add(row + col)
        self.na.add(row - col)
    
        self.DFS(n, row + 1, cur_state + [col]) # [] + [5] + [6] = [5, 6]

        self.cols.remove(col)
        self.pie.remove(row + col)
        self.na.remove(row - col)
```



## Two-ended BFS 双向BFS



## 启发式搜索 Heuristic Search (A*)

### A* search 代码

```python
def AstarSearch(graph, start, end):
  pq = collections.priority_queue() # 优先级 -> 估价函数  优先队列
  pq.append([start])
  visited.add(start)
  
  while pq:
    node = pq.pop() # can we add more intelligence here ?
    visited.add(node)
    
    process(node)
    nodes = generate_related_nodes(node)
    unvisited = [node for node in nodes if node not in visited] #在递归遍历的过程中，判断node是否已经被遇到过，如果遇到过就跳过
    pq.push(unvisited)
```



### 估价函数

启发式函数: h(n)，它用来评价哪些结点最有希望的是一个我们要找的结点，h(n) 会返回一个非负实数,也可以认为是从结点n的目标结点路径的估计成本。

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。

## 第十五课 高级树、AVL 树和红黑树

## 复习 二叉搜索树 Binary Search Tree(BST)

二叉搜索树，也称二叉排序树、有序二叉树(Ordered Binary Tree)、排序二叉树(Sorted Binary Tree)，是指一棵空树或者具有下列性质的二叉 树:

1. 左子树上所有结点的值均小于它的根结点的值;
2. 右子树上所有结点的值均大于它的根结点的值;
3. 以此类推:左、右子树也分别为二叉查找树。 (这就是 重复性!)

### 保证性能的关键

1. 保证二维维度! —> 左右子树结点平衡(recursively)
2. Balanced
3. https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree

## AVL 树 （平衡二叉搜索树）

1. 发明者 G. M. Adelson-Velsky 和 Evgenii Landis
2. 每个结点存 Balance Factor(平衡因子): 是它的左子树的高度减去它的右子树的高度(有时相反)。 balancefactor={-1, 0, 1}
3. 通过旋转操作来进行平衡(四种：左旋、右旋、左右旋、右左旋)
4. https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree

不足:结点需要存储额外信息、且调整次数频繁

## 红黑树 （Red-black Tree）

红黑树是一种近似平衡的二叉搜索树(Binary Search Tree)，它能够确保任何一 个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉 搜索树:

• 每个结点要么是红色，要么是黑色
 • 根结点是黑色
 • 每个叶结点(NIL结点，空结点)是黑色的。
 • 不能有相邻接的两个红色结点
 • 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。

关键性质：从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

### 【AVL树】 和 【红黑树】 对比

• AVL trees provide faster lookups than Red Black Trees because they are more strictly balanced.

- Red Black Trees provide faster insertion and removal operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
- AVL trees store balance factors or heights with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
- Red Black Trees are used in most of the language libraries
   like map, multimap, multisetin C++whereas AVL trees are used in databases where faster retrievals are required.

----------------------

# Week_08

------------------------

## 位运算

### 位运算符

左移	<<

右移	>>

按位或	|

按位与	&

按位取反	~

按位异或(相同为零不同为一)	^



### XOR-异或

异或:相同为 0，不同为 1。也可用“不进位加法”来理解。 异或操作的一些特点:

 x^0=x

x^1s=~x //**注意** **1s = ~0**

x^(~x)=1s

x^x=0

c=a^b => a^c=b,b^c=a //交换两个数 a^b^c=a^(b^c)=(a^b)^c //associative

###指定位置的位运算

\1. 将x最右边的n位清零:x&(~0<<n)
 \2. 获取x的第n位值(0或者1):(x>>n)&1
 \3. 获取x的第n位的幂值:x&(1<<n)
 \4. 仅将第n位置为1:x|(1<<n)
 \5. 仅将第n位置为0:x&(~(1<<n))
 \6. 将x最高位至第n位(含)清零:x&((1<<n)-1)

###实战位运算要点

- 判断奇偶:
   x%2==1 —>(x&1)==1 x%2==0 —>(x&1)==0

- x>>1—>x/2.
   即: x=x/2; —> x=x>>1;

  mid=(left+right)/2; —> mid=(left+right)>>1;

- X=X&(X-1)清零最低位的1

- X&-X=>得到最低位的1     ####  -X表示取反再加1

- X&~X=>0

### N皇后的位运算解法 - Python

```python
def totalNQueens(self, n):
  if n < 1: return []
  self.count = 0
  self.DFS(n, 0, 0, 0)
  return self.count

def DFS(self, n, row, cols, pie, na):
  # recursion terminator
  if row >= n:
    self.count += 1
    return
  
  bits = (~(cols | pie | na)) & ((1 << n) - 1) #得到当前所有的空位,1表示空位，可以放，0表示不能放;将x最高位至第n位(含)清零:x&((1<<n)-1)
  
  while bits:
    p = bits & -bits #取到最低位的1;-X表示取反再加1
    bits = bits & (bits - 1) #表示在p位置上放入皇后；X=X&(X-1)清零最低位的1
    self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1) # (X | p) 表示pie或na在p位置由0变为1，即相应位置被pie或na占据了
    # 不需要revert cols, pie, na 的状态
```



## 布隆过滤器 Bloom Filter

### Bloom Filter vs Hash Table

一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。

优点是空间效率和查询时间都远远超过一般的算法，
缺点是有一定的误识别率和删除困难。

自己理解：当检索到一个元素不在一个集合中时，可以确定这个集合中没有这个元素；当检索到一个元素在一个集合中时，实际上这个集合不一定含有该元素。

### 布隆过滤器 Python 实现

```python
from bitarray import bitarray # https://pypi.org/project/bitarray/
import mmh3 # https://www.jb51.net/article/171500.htm

import mmh3
class BloomFilter:
  def __init__(self, size, hash_num):
    self.size = size #二进制向量长度
    self.hash_num = hash_num #用多少个二进制位来表示一个元素
    self.bit_array = bitarray(size) #创建一个bitarray(二进制向量)实例
    self.bit_array.setall(0) #将这个二进制向量实例的每一位都初始华为0
    
	def add(self, s): #将元素添加到集合里
    for seed in range(self.hash_num):
      result = mmh3.hash(s, seed) % self.size #s元素经过hash变换后得到一串数字，除余表示只留size里的那一段
      self.bit_array[result] = 1 #将hash变换后对应的位置变为1
      
	def lookup(self, s): #检索元素是否在集合里
    for seed in range(self.hash_num):
      result = mmh3.hash(s, seed) % self.size
      if self.bit_array[result] == 0: #只要有一个对应的位为空，则元素不在集合中
        return "Nope"
		return "Probably" #所有对应位不为空，则该元素有可能在集合中

bf = BloomFilter(500000, 7)
bf.add("geektime")
print (bf.lookup("geektime"))
print (bf.lookup("nyd"))
```

## LRU Cache

两个要素: 大小 、替换策略

Hash Table + Double LinkedList

时间复杂度：
O(1) 查询
O(1) 修改、更新

## 替换策略

LFU - least frequently used

LRU - least recently used

## LRU Cache — Python实现代码

```python
class LRUCache(object):
  
  def __init__(self, capacity): #capacity为容量
    self.dic = collections.OrderedDict() #有序字典
    self.remain = capacity #remain为还能再放下几个，一开始是capycity，因为全部为空
    
	def get(self, key): #查询
    if key not in self.dic:
      return -1 #如果没有就返回-1
    v = self.dic.pop(key) #如果有，就取出
    self.dic[key] = v #放入末尾，因为是有序字典
    return v
  
  def put(self, key, value):
    if key in self.dict: #如果字典里有，就取出
      self.dic.pop(key)
    else:
      if self.remain > 0: #如果字典里没有，且还有空位，那么空位就-1
        self.remain -= 1
      else:
        self.dic.popitem(last=False) #如果字典里没有，且没有空位，那么就弹出第一个
		self.dic[key] = value #最后把要加入的元素加在有序字典的末尾
```



## 排序

## 排序算法

### 1.  比较类排序:

通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也称为非线性时间比较类排序。

### 2. 非比较类排序:

不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。



## 初级排序 - O(n^2)

1. 选择排序(Selection Sort) 每次找最小值，然后放到待排序数组的起始位置。

2. 插入排序(Insertion Sort) 从前到后逐步构建有序序列;对于未排序数据，在已排序序列中从后 向前扫描，找到相应位置并插入。

3. 冒泡排序(Bubble Sort) 嵌套循环，每次查看相邻的元素如果逆序，则交换。



## 高级排序 - O(N*LogN)

### 快速排序(Quick Sort)

数组取标杆 pivot，将小元素放 pivot左边，大元素放右侧，然后依 次对右边和右边的子数组继续快排;以达到整个序列有序。

快排代码 - Java

```java
public static void quickSort(int[] array, int begin, int end) {
  if (end <= begin) return;
  int pivot = partition(array, begin, end);
  quickSort(array, begin, pivot - 1);
  quickSort(array, pivot + 1, end);
}

static int partition(int[] a, int begin, int end) {
  // pivot: 标杆位置, counter: 小于pivot的元素的个数
  int pivot = end, counter = begin;
  for (int i = begin; i < end; i++) {
    if (a[i] < a[pivot]) {
      int temp = a[counter]; a[counter] = a[i]; a[i] = temp; //交换a[counter]和a[i]
      counter++; //双指针
    }
  }
  int temp = a[pivot]; a[pivot] = a[counter]; a[counter] = temp; //双指针循环结束后，将pivot放在正确的位置
  return counter; //虽然返回的只有counter，但是在过程中数组array已经被改变了
}
```

