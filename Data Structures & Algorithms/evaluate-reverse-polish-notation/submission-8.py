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
                    stack.append(num2 + num1)
                if sym == '-':
                    stack.append(num2 - num1)
                if sym == '*':
                    stack.append(num2 * num1)
                if sym == '/':
                    stack.append(int(num2/num1))

        res = int(stack.pop())
        
        return res


        