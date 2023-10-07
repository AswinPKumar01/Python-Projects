class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def push(self, item):
        # Add an element to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        # Check if the stack is empty
        return not self.items

    def peek(self):
        # Return the top element of the stack without removing it
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)

# Example Usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
assert stack.peek() == 3
assert stack.size() == 3
stack.pop()
assert stack.size() == 2
