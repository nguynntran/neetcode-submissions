class KthLargest:
    # My solution: Space complextiy will be large
    '''
    def __init__(self, k: int, nums: List[int]):
        self.array = nums
        self.k = k
        heapq.heapify(self.array)

    def add(self, val: int) -> int:
        heapq.heappush(self.array, val)
        top_k = heapq.nlargest(self.k, self.array)
        return top_k[-1]
    '''

    # Second way : Cut the heap always at the length = k 
    # The k-th element will be the first ele of min heap
    def __init__(self, k: int, nums:List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]