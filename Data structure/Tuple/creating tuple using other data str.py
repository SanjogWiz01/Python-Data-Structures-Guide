# tuple also can be creatd by string ,list, dictionary
# tuple from string
mytuple = tuple("hello")
print(mytuple)
# tuple from list
mytuple2 = tuple([1, 2, 3, 4, 5])
print(mytuple2)
# tuple from dictionary
mytuple3 = tuple({1: 'a', 2: 'b', 3
: 'c'})
print(mytuple3)  # Output will be (1, 2, 3
# as dictionary keys are taken in tuple
# tuple from set
mytuple4 = tuple({1, 2, 3, 4, 5
})
print(mytuple4)  # Output will be (1, 2, 3, 4, 5
# as set elements are taken in tuple