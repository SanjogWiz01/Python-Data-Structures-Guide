# string_reverse.py
text = "Sanjog"

# Method 1: Slicing
print("Reversed:", text[::-1])

# Method 2: Using loop
rev = ""
for char in text:
    rev = char + rev
print("Reversed (loop):", rev)

# Method 3: Using reversed() and join()
rev2 = ''.join(reversed(text))  
print("Reversed (reversed()):", rev2)
# Method 4: Using recursion
def reverse_recursive(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_recursive(s[:-1])
print("Reversed (recursion):", reverse_recursive(text))
