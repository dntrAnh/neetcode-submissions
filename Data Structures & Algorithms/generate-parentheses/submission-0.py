class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        result = []
        
        def backtrack(left, right):
            if len(s) == n * 2:
                result.append(''.join(s))
                return
            
            if left < n:
                s.append('(')
                backtrack(left + 1, right)
                s.pop()
            
            if right < left:
                s.append(')')
                backtrack(left, right + 1)
                s.pop()
        
        backtrack(0, 0)
        return result