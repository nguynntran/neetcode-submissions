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
                    tmp = (s1 + s2)
                if val == "-":
                    tmp = (s1 - s2)
                if val == "*":
                    tmp = (s1 * s2)
                if val == "/":
                    tmp = int(s1 / s2)
                stack.append(tmp)
        result = stack.pop()
        return result