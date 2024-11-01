class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = item
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            element = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return element

        else:
            raise Exception("Stack is empty")

    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1


obj = Stack(5)
obj.push(2)
obj.push(4)
obj.push(3)
print(obj.stack)

print(obj.pop())  # Output: 3
print(obj.stack)

print(obj.peek())  # Output: 4
