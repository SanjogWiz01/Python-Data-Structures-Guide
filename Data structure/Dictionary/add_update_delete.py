# dictionary_add_update_delete.py
student = {"name": "Aarav", "age": 19}

# Add new key-value pairs
student["course"] = "Data Science"
student["city"] = "Kathmandu"

# Update values
student["age"] = 20

# Delete keys
del student["city"]

print("Updated Dictionary:", student)
print("All Keys:", student.keys()) #keys() method to get all keys in the dictionary 
print("All Values:", student.values())
print("All Items:", student.items())