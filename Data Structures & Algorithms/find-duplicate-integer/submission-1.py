class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # First way : Negative marking
        '''
        for val in nums:
            idx = abs(val)

            if nums[idx] < 0:
                return idx
            nums[idx] = - nums[idx]
        
        return -1
        '''
        # Second way: Fast - Slow Pointer
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow