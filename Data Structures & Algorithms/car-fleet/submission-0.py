class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = []

        for i, pos in enumerate(position):
            sort.append((pos, speed[i]))
        
        sort = sorted(sort, reverse = True)

        res = 0
        stack = []

        for car in sort:
            steps = (target - car[0]) / car[1]
            if len(stack) == 0:
                stack.append(steps)
            else:
                curSteps = stack[-1]

                if curSteps < steps:
                    stack.append(steps)
                    


        return len(stack)

        