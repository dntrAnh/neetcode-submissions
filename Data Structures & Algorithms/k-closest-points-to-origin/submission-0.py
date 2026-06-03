class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_calculator(pointA, pointB):
            Ax_coord, Ay_coord = pointA[0], pointA[1]
            Bx_coord, By_coord = pointB[0], pointB[1]
            return math.sqrt((Ax_coord - Bx_coord) ** 2 + (Ay_coord - By_coord) ** 2)
        
        max_heap = [] # (dist, [point])
        for point in points:
            dist = distance_calculator(point, [0, 0])
            heapq.heappush(max_heap, (dist, point))
        
        result = []
        for _ in range(k):
            valid = heapq.heappop(max_heap)
            result.append(valid[1])
        
        return result