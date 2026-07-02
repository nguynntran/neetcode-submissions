class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        def addArea(r,c):
            if (r < 0 or r == rows) or (c < 0 or c == cols) or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            queue.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r,c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                grid[r][c] = dist
                addArea(r + 1, c)
                addArea(r - 1, c)
                addArea(r, c + 1)
                addArea(r, c - 1)
            dist += 1

        