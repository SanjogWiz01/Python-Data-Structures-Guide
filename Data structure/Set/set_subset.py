# Topic: Set Comparisons

a = {1, 2}
b = {1, 2, 3}

print("a is subset of b:", a.issubset(b))
print("b is superset of a:", b.issuperset(a))
print("a and b are disjoint:", a.isdisjoint({4, 5}))