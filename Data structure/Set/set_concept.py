a={1,2,2,1,2,4} # no duplicate values

nums = [1, 2, 2, 3, 4, 4]
print("Without duplicates:", list(set(nums)))

# Q2: Check if two lists have common elements
a = [1, 2, 3]
b = [3, 4, 5]
print("Common elements exist:", bool(set(a) & set(b)))

# Q3: Count unique characters
s = "hello world"
print("Unique characters:", len(set(s)))