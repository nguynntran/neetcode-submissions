class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()
        count = 0
        def dfs(node):
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visit:
                count += 1
                dfs(node)

        return count