# 47. Permutations II
# 47. 全排列 II


# https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
# 深度优先 dfs
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy()) #这里用copy()是因为path列表会不停地改变
                return
            for i in range(size):
                if not used[i]:
                    
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()
        
        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res



# https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
# 递归 回溯
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        res = []

        def backtrack(index):
            if index == len(nums) and nums[:] not in res:
                res.append(nums[:])
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index+1)
                nums[index], nums[i] = nums[i], nums[index]
        
        backtrack(index=0)
        return res

# 改编第46题
# 递归 回溯
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: # 经过排序后可以这么看是否重复
                    continue
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        nums.sort() # 排序
        backtrack(nums, [])
        return res

# 迭代器
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(itertools.permutations(nums)))



