class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parn = {
            ")":"(",
            "]":'[',
            "}":"{"
        }
        for ch in s:
            if not stack and ch in parn:
                return False
            if stack and  parn.get(ch) == stack[-1]:
                stack.pop()
                continue
            stack.append(ch)
        
        return len(stack)==0
