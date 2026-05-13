class MinStack:

    def __init__(self):
        self.mn = float("Infinity")
        self.stack = []
        self.minStack=[]

    def push(self, val: int) -> None:
        self.mn = min(self.mn, val)
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1])) 

    def pop(self) -> None:
        if not self.stack:
            return None
        self.minStack.pop()
        return self.stack.pop()
       

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1]
