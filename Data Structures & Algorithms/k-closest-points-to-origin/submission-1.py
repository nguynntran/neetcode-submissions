class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # res = []
        # heap = []
        # for point in points:
        #     x, y = point[0], point[1]
        #     heapq.heappush(heap, (x**2 + y**2, point))
        # while len(res) < k:
        #     val = heapq.heappop(heap)[1]
        #     res.append(val)
        # return res
        heap = []
        for point in points:
            d = (point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (-d, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap] 