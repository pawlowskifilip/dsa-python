class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print("stack overflow")
        else:
            self.stack.append(data)

    def printStack(self):
        return print(self.stack)

    def __str__(self):
        return " ".join([str(i) for i in self.stack])

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("stack is empty")
            return

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("stack is empty")

    def isEmpty(self):
        return self.stack == []


stck = Stack()
# stck.push(10)
stck.pop()
print(stck)
stck.printStack()
