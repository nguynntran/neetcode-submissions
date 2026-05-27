class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand (l : int, r: int) -> str:
            while (l >= 0 and r <= len(s) - 1) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]
        result = ""
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i, i + 1)
        
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        
        return result