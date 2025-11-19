# list_add_remove.py
# Adding and removing elements

fruits = ["apple", "banana", "mango"]

fruits.append("orange")      # Add to end
fruits.insert(1, "grapes")   # Add at position
print("After adding:", fruits)

fruits.remove("banana")      # Remove by value
deleted = fruits.pop()       # Remove last element
print("Removed:", deleted)
print("After removing:", fruits)
fruits.pop(1)                # Remove at position