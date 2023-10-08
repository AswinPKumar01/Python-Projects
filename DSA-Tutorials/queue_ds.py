from collections import deque

class Queue:
    def __init__(self):
        # Initialize an empty deque to store queue elements
        self.items = deque()

    def enqueue(self, item):
        # Add an element to the rear of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.items.popleft()

    def is_empty(self):
        # Check if the queue is empty
        return not self.items

    def front(self):
        # Return the front element of the queue without removing it
        if not self.is_empty():
            return self.items[0]

    def size(self):
        # Return the number of elements in the queue
        return len(self.items)

# Example Usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
assert queue.front() == 1
assert queue.size() == 3
queue.dequeue()
assert queue.size() == 2
