# 455. Assign Cookies
# 455. 分发饼干


# 双指针，while循环，自己写
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1
        return count



# 优化
# https://leetcode-cn.com/problems/assign-cookies/solution/455fen-fa-bing-gan-tan-xin-suan-fa-shuang-zhi-zhen/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i # i是得到满足的孩子序号，同时也是得到满足的孩子个数
