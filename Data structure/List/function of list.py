'''
We can add elements to a list using the following methods:

append(): Adds an element at the end of the list.
extend(): Adds multiple elements to the end of the list.
insert(): Adds an element at a specific position.
clear(): removes all items.
'''
a=[10, 20, 30, 40, 50]
a.append(60)
print("after appending the list is:", a)
a.extend([70, 80])
print("after extending the list is:", a)
a.insert(2, 25)
print("after inserting the list is:", a)
a.insert(0, 9845555)
print("after inserting the  5 thr list is:", a)
a.clear()
print("after clearing the list is:", a)