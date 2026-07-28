class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum, curSum = nums[0], 0
        l2 = 0
        while l2 < n:
            if curSum < 0:
                curSum = 0
            curSum += nums[l2]
            maxSum = max(maxSum, curSum)
            l2 += 1
        return maxSum