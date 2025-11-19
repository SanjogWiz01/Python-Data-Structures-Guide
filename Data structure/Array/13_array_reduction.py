# array_reduction.py
from functools import reduce

arr = [1,2,3,4,5]

# Sum of all elements
total = sum(arr)
print("Sum:", total)

# Product using reduce
product = reduce(lambda x,y: x*y, arr)
print("Product:", product)
