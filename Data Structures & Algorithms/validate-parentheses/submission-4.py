def isValid(cur, bracket):
    if cur == '(' and bracket == ')':
        return True
    elif cur == '{' and bracket == '}':
        return True
    elif cur == '[' and bracket == ']':
        return True
    else:
        return False


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        if len(s) % 2 != 0:
            return False

        options = ['(', '[', '{']
        for bracket in s:
            if bracket in options:
                stack.append(bracket)
            else:
                if len(stack) == 0 or not isValid(stack.pop(), bracket):
                    return False

        if len(stack) > 0:
            return False

        return True

        