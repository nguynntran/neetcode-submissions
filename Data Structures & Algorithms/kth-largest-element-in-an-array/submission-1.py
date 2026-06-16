class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = [-val for val in nums]
        heapq.heapify(self.heap)
        for _ in range(k - 1):
            heapq.heappop(self.heap)
        
        return -self.heap[0]