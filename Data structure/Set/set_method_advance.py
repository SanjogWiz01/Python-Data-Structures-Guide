# set_methods_advanced.py

a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)  # modifies a
print("After intersection_update:", a)

b.symmetric_difference_update({1,2})
print("After symmetric_difference_update:", b)
# Topic: Advanced Set Methods