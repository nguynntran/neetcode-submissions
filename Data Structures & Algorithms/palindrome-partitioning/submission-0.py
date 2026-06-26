class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)
        def is_palindrome(word):
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                    break
                i += 1
                j -= 1
            return True

        def backtrack(start):
            if start == n:
                res.append(path[:])
            
            for end in range(start, n):
                subs = s[start:end + 1]
                if is_palindrome(subs):
                    path.append(subs)
                    backtrack(end + 1)
                    path.pop()
                
        backtrack(0)
        return res
