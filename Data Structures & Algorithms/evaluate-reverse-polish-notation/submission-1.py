class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                num_stack.append(int(t))
            else:
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                if t == '+':
                    num_stack.append(num_1 + num_2)
                elif t == '-':
                    num_stack.append(num_1 - num_2)
                elif t == '*':
                    num_stack.append(num_1 * num_2)
                else:
                    num_stack.append(int(num_1 / num_2))

        return num_stack[-1]