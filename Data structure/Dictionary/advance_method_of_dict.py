# dictionary_methods_advanced.py
person = {"name": "Rita", "age": 25}
person.update({"city": "Pokhara", "role": "Data Analyst"})

print("After update:", person)

removed = person.pop("role")
print("Popped item:", removed)
print("Dictionary now:", person)

person.popitem()  # removes last inserted item
print("After popitem:", person)
