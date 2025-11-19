# dict_comphersion.py
numbers = range(1, 11)
squared_dict = {x: x**2 for x in numbers if x % 2 == 0}

print("Squared Dict (Even numbers only):", squared_dict)

# Nested comprehension: mapping numbers to their factors
factor_dict = {x: [i for i in range(1, x+1) if x % i == 0] for x in range(1, 6)}
print("Factor Dict:", factor_dict)
