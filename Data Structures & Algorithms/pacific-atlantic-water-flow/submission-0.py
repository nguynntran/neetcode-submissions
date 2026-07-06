class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevNode):
            if (r,c) in visit or r < 0 or r == rows or c < 0 or c == cols or heights[r][c] < prevNode:
                return
            visit.add((r,c))
            dfs(r - 1,c,visit,heights[r][c])
            dfs(r + 1,c,visit,heights[r][c])
            dfs(r,c - 1,visit,heights[r][c])
            dfs(r,c + 1,visit,heights[r][c])

        for h in range(rows):
            dfs(h, 0, pac, heights[h][0])
            dfs(h, cols - 1, atl, heights[h][cols - 1])
        
        for h in range(cols):
            dfs(0, h, pac, heights[0][h])
            dfs(rows - 1, h, atl, heights[rows - 1][h])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res