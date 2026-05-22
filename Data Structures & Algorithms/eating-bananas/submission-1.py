class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r
        while l <= r:
            mid = (l + r) // 2
            total_hours = 0
            for b in piles:
                total_hours += math.ceil(b / mid)
            if total_hours <= h:
                r = mid - 1
                minK = min(minK, mid)
            else:
                l = mid + 1
        return minK
