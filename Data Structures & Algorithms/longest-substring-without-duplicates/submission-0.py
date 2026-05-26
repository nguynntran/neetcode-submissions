class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        L, R = 0, 0
        longest_sub = 0
        h_set = set()
        while (R <= len(s) - 1):
            if s[R] not in h_set:
                h_set.add(s[R])
                R += 1
                longest_sub = max(longest_sub, len(s[L:R]))
            else:
                h_set.remove(s[L])
                L += 1
        return longest_sub
