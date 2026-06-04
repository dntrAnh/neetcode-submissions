class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target):
            if target == 0:
                result.append(temp[:])
                return
            elif target < 0:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                temp.pop()
        
        result = []
        temp = []
        candidates.sort()
        backtrack(0, target)
        return result