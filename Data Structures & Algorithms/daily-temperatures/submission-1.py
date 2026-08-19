class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) > 0 and temp > temperatures[stack[-1]]:
                    day = stack.pop()

                    res[day] = i - day

            stack.append(i)
        
        return res
