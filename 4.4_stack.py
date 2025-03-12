class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"{value} pushed to stack")

    def pop(self):
        if self.stack:
            print(f"{self.stack.pop()} popped from stack")
        else:
            print("Stack is empty")

stack = Stack()

stack.push(10)
stack.push(20)
stack.pop()
stack.pop()
stack.pop()
