# dictionary_copy_clear.py
employee = {"name": "Ravi", "role": "Analyst"}
# .copy can copy the element 
copy_emp = employee.copy()
print("Original:", employee)
print('copied data',copy_emp)
# Shallow copy
employee.clear()  
# Remove everything
copy_emp.clear()
print("Original (cleared):", employee)
print("Copied Dictionary:", copy_emp)