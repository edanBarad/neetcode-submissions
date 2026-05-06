class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val,val))
        else:
           self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        del self.st[-1]

    def top(self) -> int:
        return self.st[-1][0]        

    def getMin(self) -> int:
        return self.st[-1][1]