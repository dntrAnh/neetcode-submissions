class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = {}
        for i, n in enumerate(numbers):
            other = target - n
            if other in num_set:
                return [num_set[other], i + 1]
            num_set[n] = i + 1
        
        return []