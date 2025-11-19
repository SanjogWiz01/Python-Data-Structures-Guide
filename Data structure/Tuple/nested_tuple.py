# nested_tuple.py
nested = ((1, 2), (3, 4), (5, 6))

print("Second inner tuple:", nested[1])
print("First element of second tuple:", nested[1][0])
print("All elements in nested tuple:")
for inner in nested:
    for item in inner:
        print(item)
        