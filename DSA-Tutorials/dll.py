class DoublyNode:
    def __init__(self, data=None):
        # Initialize a node with data and pointers to the previous and next nodes
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with head and tail pointers
        self.head = None
        self.tail = None

    def append(self, data):
        # Add a new node with data to the end of the doubly linked list
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        # Return a list of elements in the doubly linked list
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Example Usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
assert dll.display() == [1, 2, 3]
