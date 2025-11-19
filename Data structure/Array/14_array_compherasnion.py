# array_comprehension.py

# Squares of even numbers
squares = [x**2 for x in range(1,11) if x % 2 == 0]
print("Squares:", squares)

# Flatten nested list
nested = [[1,2],[3,4],[5,6]]
flat = [x for sub in nested for x in sub]
print("Flattened Array:", flat)
