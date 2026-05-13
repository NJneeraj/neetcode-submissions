import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for tk in tokens:
            if stack and tk in ops:
               right = stack.pop()
               left = stack.pop()
               res=ops[tk](int(left),int(right))
               stack.append(res)
            else:
                stack.append(tk)

        return int(stack[0])