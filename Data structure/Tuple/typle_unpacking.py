
person = ("Sanjog", 18, "Nepal")

# Unpack tuple values into variables
name, age, country = person

print("=== Example 1: Basic Unpacking ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}\n")


# Example 2: Unpacking with different data
car = ("Tesla", "Model 3", 2025)
brand, model, year = car

print("=== Example 2: Car Information ===")
print(f"Brand: {brand}")
print(f"Model: {model}")
print(f"Year: {year}\n")


# Example 3: Using * to collect remaining elements
numbers = (10, 20, 30, 40, 50)
first, second, *rest = numbers

print("=== Example 3: Using *rest ===")
print("First:", first)
print("Second:", second)
print("Remaining:", rest, "\n")


# Example 4: Ignoring values using underscore (_)
student = ("Aarav", 19, "Pokhara", "Computer Engineering")
name, _, _, course = student

print("=== Example 4: Ignoring Values ===")
print(f"Name: {name}")
print(f"Course: {course}\n")


# Example 5: Nested Tuple Unpacking
record = ("Nisha", (85, 90, 80))
name, (math, science, english) = record

print("=== Example 5: Nested Tuple Unpacking ===")
print(f"Name: {name}")
print(f"Marks -> Math: {math}, Science: {science}, English: {english}")
