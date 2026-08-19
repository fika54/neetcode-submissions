class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = None
        stack = []

        for sym in tokens:
            if sym not in '+-*/':
                stack.append(sym)
            else:
                num1 = int(stack.pop())
                num2  = int(stack.pop())
                
                

                if sym == '+':
                    res = num2 + num1
                if sym == '-':
                    res = num2 - num1
                if sym == '*':
                    res = num2 * num1
                if sym == '/':
                    res = int(num2/num1)
                stack.append(res)
        if res == None:
            if len(stack) > 0:
                res = int(stack.pop())
            else:
                res = 0
        
        return res


        