class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the deflection point 
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        de_point = l
        if de_point == 0 or target < nums[0]:
            l, r = de_point, len(nums) - 1
        else:
            l, r =0, de_point - 1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1