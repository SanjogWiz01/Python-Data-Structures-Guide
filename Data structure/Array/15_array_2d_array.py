# array_2d_operations.py

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Row sums
row_sums = [sum(row) for row in matrix]
print("Row sums:", row_sums)

# Column sums
col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
print("Column sums:", col_sums)
