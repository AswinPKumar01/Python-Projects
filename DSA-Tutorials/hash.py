class HashTable:
    def __init__(self):
        # Initialize an empty hash table using a dictionary
        self.table = {}

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        self.table[key] = value

    def get(self, key):
        # Retrieve the value associated with the given key
        return self.table.get(key, None)

    def remove(self, key):
        # Remove the key-value pair associated with the given key
        if key in self.table:
            del self.table[key]

# Example Usage:
hash_table = HashTable()
hash_table.insert('name', 'John')
hash_table.insert('age', 25)
assert hash_table.get('name') == 'John'
hash_table.remove('age')
