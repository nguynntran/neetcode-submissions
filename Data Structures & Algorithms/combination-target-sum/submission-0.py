class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        def backtrack(start, remain):
            if remain == 0:
                res.append(arr[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    continue
                arr.append(nums[i])
                backtrack(i, remain - nums[i])
                arr.pop()
        
        backtrack(0, target)
        return res