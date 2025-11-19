# array_filtering.py

arr = [1,2,3,4,5,6]

# Keep only even numbers
even = [x for x in arr if x % 2 == 0]
print("Even Numbers:", even)
# Keep numbers greater than 3
greater_than_3 = [x for x in arr if x > 3]
print("Numbers > 3:", greater_than_3)
# Keep numbers less than or equal to 4
less_equal_4 = [x for x in arr if x <= 4]
print("Numbers <= 4:", less_equal_4)