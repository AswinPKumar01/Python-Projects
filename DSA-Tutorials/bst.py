class TreeNode:
    def __init__(self, key=None, value=None):
        # Initialize a node with a key, value, and pointers to left and right children
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # Initialize an empty binary search tree with a root pointer
        self.root = None

    def insert(self, key, value):
        # Insert a key-value pair into the binary search tree
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        # Helper function for recursive insertion
        if not node:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # Update value if key already exists
        return node

    def search(self, key):
        # Search for the value associated with the given key in the binary search tree
        return self._search(self.root, key)

    def _search(self, node, key):
        # Helper function for recursive search
        if not node or node.key == key:
            return node.value if node else None
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# Example Usage:
bst = BinarySearchTree()
bst.insert(5, 'apple')
bst.insert(3, 'banana')
bst.insert(7, 'orange')
assert bst.search(3) == 'banana'
