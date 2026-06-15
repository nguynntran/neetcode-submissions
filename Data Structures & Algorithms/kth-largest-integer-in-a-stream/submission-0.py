class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = nums
        self.k = k
        heapq.heapify(self.array)

    def add(self, val: int) -> int:
        heapq.heappush(self.array, val)
        top_k = heapq.nlargest(self.k, self.array)
        return top_k[-1]
