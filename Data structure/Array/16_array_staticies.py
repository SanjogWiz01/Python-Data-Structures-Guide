# array_statistics.py

arr = [5,2,7,3,5,2]

# Mean
mean = sum(arr)/len(arr)
print("Mean:", mean)

# Median
arr_sorted = sorted(arr)
n = len(arr)
median = (arr_sorted[n//2] if n % 2 != 0 else (arr_sorted[n//2-1]+arr_sorted[n//2])/2)
print("Median:", median)

# Mode
from collections import Counter
data = Counter(arr)
mode = [k for k,v in data.items() if v == max(data.values())]
print("Mode:", mode)
# Range
data_range = max(arr) - min(arr)
print("Range:", data_range)
# Variance
variance = sum((x - mean) ** 2 for x in arr) / len(arr)
print("Variance:", variance)
# Standard Deviation
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)
# Percentiles
percentiles = [25, 50, 75]
percentile_values = {}
