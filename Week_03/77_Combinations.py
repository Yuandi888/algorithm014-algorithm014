# 77. Combinations
# 77. 组合

# https://leetcode-cn.com/problems/combinations/solution/zu-he-by-leetcode/
# 递归 回溯
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr) #参数上一层的(i,curr)变成了(i+1,curr+i)
                curr.pop()
        
        output = []
        backtrack()
        return output


# https://leetcode-cn.com/problems/combinations/solution/pythonzu-he-by-jutraman/
# 迭代器
# import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1),k))