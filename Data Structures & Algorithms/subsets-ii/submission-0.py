class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        def traverse(idx, curr_subset):
            result.add(tuple(curr_subset))
            
            for i in range(idx, len(nums)):
                curr_subset.append(nums[i])
                traverse(i + 1, curr_subset)
                curr_subset.pop()

        traverse(0, [])
        return [list(s) for s in result]