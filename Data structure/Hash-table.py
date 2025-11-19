# manual_hash_table.py

class HashTable:
    def __init__(self, size):
        self.size = size
        # Each bucket is a list to handle collisions (chaining)
        self.table = [[] for _ in range(size)]

    # Simple hash function: sum of ASCII codes % table size
    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self._hash(key)
        # Check if key exists, update if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Otherwise, append new key-value pair
        self.table[index].append((key, value))

    # Search for a key
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    # Delete a key
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False  # Key not found

    # Display hash table
    def display(self):
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    ht = HashTable(5)

    # Insert key-value pairs
    ht.insert("name", "Sanjog")
    ht.insert("age", 18)
    ht.insert("city", "Pokhara")
    ht.insert("job", "Data Scientist")
    ht.insert("country", "Nepal")

    ht.display()

    # Search
    print("\nSearch 'city':", ht.search("city"))
    print("Search 'age':", ht.search("age"))
    print("Search 'salary':", ht.search("salary"))  # Not in table

    # Update
    ht.insert("age", 19)
    print("\nAfter updating age:")
    ht.display()

    # Delete
    ht.delete("job")
    print("\nAfter deleting job:")
    ht.display()
