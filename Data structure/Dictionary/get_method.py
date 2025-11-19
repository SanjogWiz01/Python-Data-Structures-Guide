# dictionary_get_method.py
person = {"name": "Sita", "age": 22}

# Access safely
print("Name:", person.get("name")) # existing key person["name"]
print("Age:", person.get("age"))
print("Hobby:", person.get("hobby", "Not found"))  # default value
print("City:", person.get("city", "Unknown"))  # default value