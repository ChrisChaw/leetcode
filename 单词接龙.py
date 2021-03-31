class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        如果一开始就构建图，每一个单词都需要和除它以外的另外的单词进行比较，复杂度是 O(N*wordLen)，这里 N 是单词列
        表的长度；
        为此，我们在遍历一开始，把所有的单词列表放进一个哈希表中，然后在遍历的时候构建图，每一次得到在单词列表里可以转
        换的单词，复杂度是 O(26*wordLen)，借助哈希表，找到邻居与N无关；
        使用 BFS 进行遍历，需要的辅助数据结构是：
        队列；
        visited 集合。说明：可以直接在 wordSet (由 wordList 放进集合中得到)里做删除。但更好的做法是新开一个哈希         表，遍历过的字符串放进哈希表visited里。该做法具有普遍意义。绝大多数在线测评系统和应用场景都不会在意空间开销。
        """
        from collections import deque
        word_set = set(wordList)  # 先建立包含列表里所有词的哈希表
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:  # 把开始词从哈希表里移除
            word_set.remove(beginWord)
        queue = deque()  # 建立一个双端队列
        queue.append(beginWord)  # 把开始词加到双端队列里
        visited = set(beginWord)  # 把开始词放到visited集合里 visited记录已遍历过的字符串
        word_len = len(beginWord)  # 记录开始词的长度
        step = 1  # 初始化路径长度为1
        while queue:  # 只要双端队列不为空 就循环
            current_size = len(queue)  # 保存当前双端队列里单词个数
            for i in range(current_size):
                word = queue.popleft()  # 把双端队列里的第一个词(开始词))移出双端队列 记录这个词为word

                word_list = list(word)  # 把移出双端队列的这个词放到列表word_list里
                for j in range(word_len):  # 移出双端队列的词的每个字符索引记录为j
                    origin_char = word_list[j]  # 记录移出双端队列的词的字符为origin_char

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)  # 把word_list列表里存的单词的每个字符替换为a~z
                        next_word = ''.join(word_list)  # 把字符拼接起来 得到开始词的衍生词 next_word
                        if next_word in word_set:  # 如果这个衍生词在最先建立的哈希表里
                            if next_word == endWord:  # 如果衍生词就是结束词
                                return step + 1  # 图的路径长度就是原来的长度+1
                            if next_word not in visited:  # 如果这个衍生词不在visited集合里
                                queue.append(next_word)  # 把这个衍生词加入到双端队列queue里
                                visited.add(next_word)  # 紧接着 把这个衍生词加到visited集合里 记录已遍历过
                    word_list[j] = origin_char  # 移出双端队列的词的第j个索引的字符 赋值给 存放移出双端队列的词的列表里的j号索引位置的字符
            step += 1  # 路径长度+1
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)
