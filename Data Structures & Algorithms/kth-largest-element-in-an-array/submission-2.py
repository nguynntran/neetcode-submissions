class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # First way:
        '''
        self.heap = [-val for val in nums]
        heapq.heapify(self.heap)
        for _ in range(k - 1):
            heapq.heappop(self.heap)
        
        return -self.heap[0]
        '''
        # Second way 
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]