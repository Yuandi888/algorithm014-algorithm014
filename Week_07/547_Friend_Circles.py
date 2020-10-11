# 547. Friend Circles
# 547. 朋友圈

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
    def findCurcleNum(self, M: List[List[int]]) -> int:
        if not M: return 0

        n = len(M)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)

        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root] #一直向上找到根
        while p[i] != i: #非根节点
            x = i; p[x] = root; i = p[i]
        return root