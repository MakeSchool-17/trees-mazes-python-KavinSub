class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() is False:
            return self.items.pop(len(self.items) - 1)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(3)
    stack.push(2)
    print(stack.items)
    print(stack.pop())
    print(stack.items)
