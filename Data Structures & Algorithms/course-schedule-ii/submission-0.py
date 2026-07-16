class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list) # Adjacent list
        for a, b in prerequisites:
            graph[b].append(a)
        state = [0] * numCourses

        result = []
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            result.append(node)
            return True
        for node in range(numCourses):
            if state[node] == 0:
                if not dfs(node):
                    return []

        return result[::-1] 
                