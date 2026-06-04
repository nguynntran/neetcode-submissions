class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for val in nums:
            idx = abs(val)

            if nums[idx] < 0:
                return idx
            nums[idx] = - nums[idx]
        
        return -1