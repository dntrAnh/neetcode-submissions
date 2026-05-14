class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = dict()
        result = []
        for idx, num in enumerate(nums):
            other = target - num
            if other in num_set:
                return [num_set[other], idx]
            num_set[num] = idx 
        
        return []