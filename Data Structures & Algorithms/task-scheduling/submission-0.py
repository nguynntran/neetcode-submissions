class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts= Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        queue = []
        time = 0
        while heap or queue:
            time += 1
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task < 0:
                    queue.append([task, time + n])
            if queue and queue[0][1] == time:
                val = queue.pop(0)
                heapq.heappush(heap, val[0])
        
        return time
