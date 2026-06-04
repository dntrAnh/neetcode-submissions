class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def traverse(idx, subset):
            result.append(subset[:])
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                traverse(i + 1, subset)
                subset.pop()
        
        traverse(0, [])
        return result