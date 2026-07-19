class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(src, tar, visit):
            if src == tar:
                return True
            visit.add(src)
            for neighbor in graph[src]:
                if neighbor not in visit:
                    if dfs(neighbor, tar, visit):
                        return True
            return False
        
        for a, b in edges:
            if dfs(a, b, set()):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)
        
        return []