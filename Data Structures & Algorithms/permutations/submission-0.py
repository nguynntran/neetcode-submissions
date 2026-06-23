class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []
        n = len(nums)
        track = [False] * n
        def backtrack(start):
            if len(arr) == n:
                res.append(arr[:])
                return
            
            for i in range(n):
                if track[i] == False:
                    arr.append(nums[i])
                    track[i] = True
                    backtrack(i + 1)
                    track[i] = False
                    arr.pop()
            
        backtrack(0)
        return res
