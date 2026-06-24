class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def backtrack(open, close):
            if len(s) == 2*n:
                res.append("".join(s))
                return
            
            if open < n:
                s.append("(")
                backtrack(open + 1, close)
                s.pop()
            if close < open:
                s.append(")")
                backtrack(open, close + 1)
                s.pop()
        
        backtrack(0,0)
        return res