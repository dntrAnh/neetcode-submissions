class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def feasible(speed):
            total = 0
            for p in piles:
                total += math.ceil(p / speed)
            
            return total <= h 
        
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                result = mid 
                right = mid - 1
            else: 
                left = mid + 1
        
        return result 