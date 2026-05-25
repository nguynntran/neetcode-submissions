class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[n - 1]
        if n == 2:
            return max(nums[0], nums[1])
        def rob_linear(idx1 : int, idx2 :int, nums : List[int]):
            nums = nums[idx1 : idx2 + 1]
            n = len(nums)
            if n == 1:
                return nums[n - 1]
            rob = [0] * n
            rob[0], rob[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                rob[i] = max(rob[i - 1], nums[i] + rob[i - 2])
            return rob[n - 1]
        case1 = rob_linear(0, n - 2, nums)
        case2 = rob_linear(1, n - 1, nums)
        return max(case1, case2)