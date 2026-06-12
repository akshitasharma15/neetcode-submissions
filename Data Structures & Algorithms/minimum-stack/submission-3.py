class MinStack:


    def __init__(self):
        self.min_stack = []
        self.tmp_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.tmp_stack:
            self.tmp_stack.append(val)
        else:
            if val <= self.tmp_stack[-1]:
                self.tmp_stack.append(val)


    def pop(self) -> None:
        if self.min_stack[-1] == self.tmp_stack[-1]:
            self.tmp_stack.pop()
        self.min_stack.pop()
        
        
    def top(self) -> int:
        return self.min_stack[-1] 

    def getMin(self) -> int:
        return self.tmp_stack[-1]


        
