# dictionary_merge_and_unpacking.py
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Method 1: update()
merged = d1.copy()
merged.update(d2)
print("Merged using update:", merged)

# Method 2: Unpacking
merged2 = {**d1, **d2}
print("Merged using unpacking:", merged2)
