class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        arr = []

        def backtrack(start, remainder):
            if remainder == 0:
                res.append(arr[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remainder:
                    continue
                arr.append(candidates[i])
                backtrack(i + 1, remainder - candidates[i])
                arr.pop()
        
        backtrack(0, target)
        return res