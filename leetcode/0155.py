class MinStack:

    def __init__(self):
        self.min = math.inf
        self.stack = []
        

    def push(self, value: int) -> None:
        self.min = min(value, self.min)
        node = {
            'value': value,
            'min': self.min
        }

        self.stack.append(node)
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

        if len(self.stack) == 0:
            self.min = math.inf
        else:
            self.min = self.stack[len(self.stack)-1]['min']
        

    def top(self) -> int:
        n = len(self.stack)
        if n == 0: 
            return null
        return self.stack[len(self.stack)-1]['value']
        

    def getMin(self) -> int:
        return self.min
        