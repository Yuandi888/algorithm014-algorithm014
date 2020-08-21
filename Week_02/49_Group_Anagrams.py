
# 49. Group Anagrams
# 49. 字母异位词分组

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            key = tuple(sorted(i))
            dict[key] = dict.get(key, []) + [i]
        return list(dict.values())
