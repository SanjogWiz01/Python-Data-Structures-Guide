# Topic: List Comprehension

squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)