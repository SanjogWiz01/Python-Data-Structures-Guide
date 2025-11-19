# list_student_marks_project.py
# Author: Sanjog Don
# Description: A small project using lists to handle student marks

marks = []

n = int(input("How many subjects? "))

for i in range(n):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

print("\n📊 RESULT 📊")
print("Marks List:", marks)
print("Total Marks:", sum(marks))
print("Average Marks:", round(sum(marks) / len(marks), 2))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Bonus: show marks sorted
print("Sorted Marks:", sorted(marks))
