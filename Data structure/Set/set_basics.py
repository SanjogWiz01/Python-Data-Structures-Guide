# set_basics.py
# Creating, adding, removing elements in a set

# Creating sets
my_set = {1, 2, 3, 4}
empty_set = set()  # empty set

# Adding elements
my_set.add(5)
my_set.update([6, 7])

# Removing elements
my_set.remove(2)  # raises KeyError if not exists
my_set.discard(10)  # safe removal

print("My Set:", my_set)
