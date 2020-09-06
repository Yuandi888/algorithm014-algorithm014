# 127. Word Ladder
# 127. 单词接龙

'''
函数：defaultdict( type )
其传入参数必须是type, 例如 int, list, set等，而返回的默认值，就是这些type下的默认值，例如int返回的默认值是0，list是空list等

defaultdict与普通dict的最大作用在于：
你可以直接call一个不存在的key， 如果不存在这个key，那就先直接创建这个key，并根据默认值的设置，赋值value，而后在继续操作。
省去了
dict[new] = dict.get(new, default = [])
然后才能使用dict[new]来进一步操作。
相比之下：你可放心大胆的用：defaultdict[new] 管他有没有。

作者：allen-238
链接：https://leetcode-cn.com/problems/word-ladder/solution/python-shen-du-jiang-jie-bfsde-jie-gou-by-allen-23/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 单向广度优先
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        L = len(beginWord)

        all_combo_dict = defaultdict(list) # all_combo_dict 得到 defaultdict(list, {})
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        '''	
        key是中间状态，value是含有相同中间状态的词组成的列表
        all_combo_dict =
        defaultdict(list,
            {'*ot': ['hot', 'dot', 'lot'],
            'h*t': ['hot'],
            'ho*': ['hot'],
            'd*t': ['dot'],
            'do*': ['dot', 'dog'],
            '*og': ['dog', 'log', 'cog'],
            'd*g': ['dog'],
            'l*t': ['lot'],
            'lo*': ['lot', 'log'],
            'l*g': ['log'],
            'c*g': ['cog'],
            'co*': ['cog']})
        '''
        # Queue for BFS
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited: # 没有被访问过的就加入队列
                        visited[word] = True
                        queue.append((word, level + 1))
                # all_combo_dict[intermediate_word] = []
        return 0

