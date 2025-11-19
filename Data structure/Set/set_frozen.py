# frozen_set.py

# Immutable set
fs = frozenset([1, 2, 3])
# fs.add(4)  # Error: cannot modify

print("Frozen Set:", fs)
# fs.add(4)  # Error: cannot modify
print("After trying to add 4:", fs)
print("Is 2 in frozen set?", 2 in fs)
print(fs.pop())  # Error: 'frozenset' object has no attribute 'pop'
print("After trying to pop an element:", fs)