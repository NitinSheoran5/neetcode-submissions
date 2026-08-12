class Solution:
    def isValid(self, s1: str) -> bool:
        stack = []
        closingBrackets = [']', ')', '}']

        for s in s1:
            match s:
                case ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                case ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                case '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                case _:
                    stack.append(s)
        if len(stack) > 0:
            return False
        return True
        