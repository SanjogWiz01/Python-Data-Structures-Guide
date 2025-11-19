# dictionary_nested.py
students = {
    "A01": {"name": "Sanjog", "age": 18},
    "A02": {"name": "Nisha", "age": 19}
}

print("All Students:")
for roll, info in students.items():
    print(f"Roll: {roll}, Name: {info['name']}, Age: {info['age']}")
print("Student A01 Name:", students["A01"]["name"])
print("Student A02 Age:", students["A02"]["age"])