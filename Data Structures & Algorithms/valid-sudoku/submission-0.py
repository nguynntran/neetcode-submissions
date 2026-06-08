class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create hash sets to check the duplicate:
        hash_row = [set() for _ in range(9)]
        hash_col = [set() for _ in range(9)]
        hash_box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                b = (r // 3) * 3 + (c // 3)
                if val in hash_row[r] or val in hash_col[c] or val in hash_box[b]:
                    return False
                hash_row[r].add(val)
                hash_col[c].add(val)
                hash_box[b].add(val)
        
        return True

        
