class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points:
            x, y = point[0], point[1]
            heapq.heappush(heap, (x**2 + y**2, point))
        while len(res) < k:
            val = heapq.heappop(heap)[1]
            res.append(val)
        return res
