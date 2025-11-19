# student_marks_tuple.py
math = int(input("Enter Math marks: "))
physics = int(input("Enter Physics marks: "))
computer = int(input("Enter Computer marks: "))

marks = (math, physics, computer)

total = sum(marks)
average = total / len(marks)
highest = max(marks)

print("\nMarks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", min(marks))