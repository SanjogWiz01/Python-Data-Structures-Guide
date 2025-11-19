# defaultdict_counter.py
from collections import defaultdict, Counter

# defaultdict example: counting occurrences
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = defaultdict(int)
for fruit in fruits:
    fruit_count[fruit] += 1
print("DefaultDict Count:", dict(fruit_count))

# Counter example: most common elements
counter = Counter(fruits)
print("Counter Most Common:", counter.most_common(2))
print("Counter Elements:", list(counter.elements()))