class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def find(r,c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            return 1 + find(r + 1,c) + find(r - 1,c) + find(r,c + 1) + find(r,c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    max_area = max(max_area, find(r,c))
        
        return max_area