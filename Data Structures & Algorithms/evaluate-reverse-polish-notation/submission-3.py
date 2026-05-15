class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        opes = "+-*/"
        stack = []
        for val in tokens:
            if val not in opes:
                stack.append(int(val))
            else:
                s2 = stack.pop()
                s1 = stack.pop()
                if val == "+":
                    stack.append(s1 + s2)
                if val == "-":
                    stack.append(s1 - s2)
                if val == "*":
                    stack.append(s1 * s2)
                if val == "/":
                    stack.append(int(s1 / s2))
        result = stack.pop()
        return result