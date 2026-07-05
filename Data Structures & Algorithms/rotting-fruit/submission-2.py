class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten_queue = deque()
        visited = set()
        fresh = 0
        def rotten(r,c):
            nonlocal fresh
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visited:
                return
            if grid[r][c] == 1:
                rotten_queue.append((r,c))
                visited.add((r,c))
                fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_queue.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        minute = 0
        while rotten_queue:
            minute += 1
            for _ in range(len(rotten_queue)):
                r,c = rotten_queue.popleft()
                rotten(r - 1, c)
                rotten(r + 1, c)
                rotten(r, c - 1)
                rotten(r, c + 1)
        
        return minute - 1 if fresh == 0 else -1