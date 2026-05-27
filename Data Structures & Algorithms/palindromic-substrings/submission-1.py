class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 0
        def expand(l : int, r : int) -> str:
            count = 0
            while (l >= 0 and r <= len(s) - 1 and s[l] == s[r]):
                l -= 1
                r += 1
                count += 1
            return count
        for i in range(len(s)):
            res += expand(i,i)
            res += expand(i, i + 1)

        return res