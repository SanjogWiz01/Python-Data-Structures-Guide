# Topic: Adding and Removing Elements

s = {1, 2, 3}
s.add(4)
print("After add:", s)

s.remove(2)
print("After remove:", s)

s.discard(10)  # No error if not found
print("After discard:", s)

popped = s.pop() 
print("Popped element:", popped) # removes and returns an arbitrary element
print("After pop:", s)

s.clear()
print("After clear:", s)