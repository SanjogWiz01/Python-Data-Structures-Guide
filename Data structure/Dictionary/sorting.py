# dictionary_sorting.py
scores = {"Rita": 88, "Aarav": 95, "Sanjog": 91}

sorted_by_key = dict(sorted(scores.items())) # Sort by keys (ascending) 
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

print("Sorted by Key:", sorted_by_key)
print("Sorted by Value (desc):", sorted_by_value)
