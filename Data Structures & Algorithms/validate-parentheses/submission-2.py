class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if not stack:
                    return False
                last = stack.pop()
                if (c == ')' and last != '(') or \
                    (c == '}' and last != '{') or \
                    (c == ']' and last != '['):
                    return False 
        
        return len(stack) == 0