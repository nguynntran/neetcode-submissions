class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        track = [[False] * cols for _ in range(rows)]
        
        def backtrack(r, c, k):
            if len(word) == k:
                return True
            
            if (r < 0 or r == rows) or (c < 0 or c == cols):
                return False
            
            if board[r][c] != word[k] or track[r][c] == True:
                return False
            if board[r][c] == word[k]:
                track[r][c] = True
                found = (backtrack(r, c - 1, k + 1) or
                         backtrack(r, c + 1, k + 1) or
                         backtrack(r + 1, c, k + 1) or
                         backtrack(r - 1, c, k + 1))
                track[r][c] = False
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        
        return False