学习笔记

[TOC]



# 字典树 Trie

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

## 基本结构

字典树，即 Trie 树，又称单词 查找树或键树，是一种树形结 构。典型应用是用于统计和排 序大量的字符串(但不仅限于 字符串)，所以经常被搜索引 擎系统用于文本词频统计。

它的优点是:最大限度地减少无谓的字符串比较，查询效率比哈希表高。



## 基本性质

1. 结点本身不存完整单词;

2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串;

3. 每个结点的所有子结点路径代表的字符都不相同。



## 核心思想

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





# 并查集 Disjoint Set

并查集属于比较跳跃式的数据结构，如果不会那就是压根不会，如果一会的话那就会用就行，没有太多可进行发展和自由发挥的空间或非常强的随机应变。这类题目比较死，主要是调用现成的代码，把模版记好之后直接套上去用即可。

判断什么问题可以使用并查集：如有多少个朋友圈，或者它属于谁，或者任意给两个人是不是朋友

## 适用场景

组团、配对问题

Group or not?



## 基本操作

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
    root = p[root] #一直往上找到最顶层的根
  while p[i] != i: # 路径压缩？
    x = i; i = p[i]; p[x] = root #将每个节点的父节点都指向root
  return root
```







