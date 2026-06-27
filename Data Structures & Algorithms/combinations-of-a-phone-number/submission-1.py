class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_dict = {"2" : ["a", "b", "c"],
                     "3" : ["d", "e", "f"],
                     "4" : ["g", "h", "i"],
                     "5" : ["j", "k", "l"],
                     "6" : ["m", "n", "o"],
                     "7" : ["p", "q", "r", "s"],
                     "8" : ["t" , "u", "v"],
                     "9" : ["w", "x", "y", "z"]}
        if not digits:
            return []
        n = len(digits)
        res = []
        arr = []
        def backtrack(index):
            if index == n:
                res.append(''.join(arr))
                return

            letters = hash_dict[digits[index]]
            for letter in letters:
                arr.append(letter)
                backtrack(index + 1)
                arr.pop()

        backtrack(0)
        return res