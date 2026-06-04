class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def traverse(idx, subset, curr_sum):
            if curr_sum == target:
                result.append(subset[:])
                return
            if curr_sum > target:
                return
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                traverse(i, subset, curr_sum + nums[i])
                subset.pop()
        
        traverse(0, [], 0)
        return result