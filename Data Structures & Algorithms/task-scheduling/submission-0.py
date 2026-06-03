class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = Counter(tasks)
        heap = []

        for freq in task_frequency.values():
            heapq.heappush(heap, -freq)
        
        time = 0
        
        while heap:
            temp = []
            for _ in range(n + 1):
                if heap:
                    temp.append(heapq.heappop(heap))
                
            for f in temp: 
                if f + 1 < 0:
                    heapq.heappush(heap, f + 1)
                    
            if heap:
                time += n + 1
            else:
                time += len(temp)
        
        return time