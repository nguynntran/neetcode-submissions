class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack[-1]
                res[top] = i - top
                stack.pop()
            stack.append(i)

        if stack:
            for ele in stack:
                res[ele] = 0
        return res
