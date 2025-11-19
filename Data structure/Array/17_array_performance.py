# array_performance.py
import time

N = 10**6
arr = list(range(N))

# Loop sum
start = time.time()
total = 0
for x in arr:
    total += x
print("Loop sum:", time.time()-start)

# List comprehension sum
start = time.time()
total = sum([x for x in arr])
print("Comprehension sum:", time.time()-start)
