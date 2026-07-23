class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbor = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                nei = word[:j] + "*" + word[j+1:]
                neighbor[nei].append(word)
        visit = set([beginWord])
        q = deque([beginWord])

        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    nei = word[:i] + "*" + word[i+1:]
                    for node in neighbor[nei]:
                        if node not in visit:
                            visit.add(node)
                            q.append(node)
            res += 1
        
        return 0