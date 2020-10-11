学习笔记

[TOC]

# 位运算

## 位运算符

左移	<<

右移	>>

按位或	|

按位与	&

按位取反	~

按位异或(相同为零不同为一)	^



## XOR-异或

异或:相同为 0，不同为 1。也可用“不进位加法”来理解。 异或操作的一些特点:

 x^0=x

x^1s=~x //**注意** **1s = ~0**

x^(~x)=1s

x^x=0

c=a^b => a^c=b,b^c=a //交换两个数 a^b^c=a^(b^c)=(a^b)^c //associative



##指定位置的位运算

\1. 将x最右边的n位清零:x&(~0<<n)
 \2. 获取x的第n位值(0或者1):(x>>n)&1
 \3. 获取x的第n位的幂值:x&(1<<n)
 \4. 仅将第n位置为1:x|(1<<n)
 \5. 仅将第n位置为0:x&(~(1<<n))
 \6. 将x最高位至第n位(含)清零:x&((1<<n)-1)



##实战位运算要点

- 判断奇偶:
   x%2==1 —>(x&1)==1 x%2==0 —>(x&1)==0

- x>>1—>x/2.
   即: x=x/2; —> x=x>>1;

  mid=(left+right)/2; —> mid=(left+right)>>1;

- X=X&(X-1)清零最低位的1

- X&-X=>得到最低位的1     ####  -X表示取反再加1

- X&~X=>0



## N皇后的位运算解法 - Python

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





# 布隆过滤器 Bloom Filter

