# dictionary_iteration.py
data = {"Nepal": "Kathmandu", "India": "Delhi", "China": "Beijing"}

print("Keys:") # Iterate over keys keys are dict keys fornt elemenntts
for country in data: 
    print(country)

print("\nValues:")
for capital in data.values():
    print(capital)

print("\nKey-Value pairs:")
for country, capital in data.items():
    print(f"{country} → {capital}")
