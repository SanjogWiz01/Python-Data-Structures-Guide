# list_nested.py
# Nested lists (lists inside lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for i in matrix:
    print(i)

print("Middle element:", matrix[1][1])
print("First row:", matrix[0])
print("Last column:", [row[2] for row in matrix])
print("Flattened:", [num for row in matrix for num in row])


# Adding a new row
matrix.append([10, 11, 12])
print("After adding a row:")
for i in matrix:
    print(i)
# Accessing an element
print("Element at (2,3):", matrix[1][2])  #
# Modifying an element
matrix[0][0] = 99
print("After modifying (1,1):")
for i in matrix:
    print(i)
    
