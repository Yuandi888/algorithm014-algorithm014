# 242. Valid Anagram
# 242. 有效的字母异位词

# 讨巧的办法 python 字符串排序
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# 网上他人解法，讨巧，通过字典，更快
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


# 通过字典
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        for j in t:
            dict_t[j] = dict_t.get(j, 0) + 1
        return dict_s == dict_t
