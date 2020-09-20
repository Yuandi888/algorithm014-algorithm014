# 221. Maximal Square
# 221. 最大正方形

# https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/
# 原始答案，空间复杂度为O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        maxSquare = maxSide * maxSide
        return maxSquare


# 优化后将空间复杂度从O(mn)降低至O(n)，但是时间复杂度增加
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns]
        for i in range(rows):
            dp.append([0] * columns)
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j==0:
                        dp[1][j] = 1
                    else:
                        dp[1][j] = min(dp[0][j], dp[1][j - 1], dp[0][j - 1]) + 1
                    maxSide = max(maxSide, dp[1][j])
            dp.pop(0)
        maxSquare = maxSide * maxSide
        return maxSquare