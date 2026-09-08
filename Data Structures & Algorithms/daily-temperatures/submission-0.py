class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i, temp in enumerate(temperatures[1:], start = 1):
            while (stack and temp > stack[-1][1]):
                top_i, _ = stack.pop()
                result[top_i] = i - top_i
            stack.append((i, temp))
        return result
            