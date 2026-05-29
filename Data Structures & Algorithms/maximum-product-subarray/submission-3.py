class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        max_dp = nums[0]
        min_dp = nums[0]

        for i in range(1, n):
            cand = (nums[i], max_dp * nums[i], min_dp * nums[i])

            max_dp = max(cand)
            min_dp = min(cand)

            res = max(res, max_dp)
        
        return res