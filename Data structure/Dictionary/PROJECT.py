# student_database_project.py
# Author: Sanjog Don
# Description: Manage student records using dictionaries

students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "age": age, "marks": marks}
    print(f"\n✅ Record added for {name}\n")

def display_students():
    if not students:
        print("\n⚠️ No records available.\n")
        return
    print("\n🎓 STUDENT RECORDS")
    print("-"*30)
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Age: {info['age']} | Marks: {info['marks']}")

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print("\nFound:", students[roll])
    else:
        print("\n❌ No record found.\n")

def update_marks():
    roll = input("Enter Roll No to update marks: ")
    if roll in students:
        new_marks = float(input("Enter new marks: "))
        students[roll]["marks"] = new_marks
        print("\n✅ Marks updated successfully!\n")
    else:
        print("\n❌ Roll number not found.\n")

while True:
    print("=== STUDENT DATABASE MENU ===")
    print("1. Add Student\n2. Display All\n3. Search\n4. Update Marks\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1': add_student()
    elif choice == '2': display_students()
    elif choice == '3': search_student()
    elif choice == '4': update_marks()
    elif choice == '5':
        print("\n👋 Exiting... Have a great day, Data Scientist!")
        break
    else:
        print("\n❌ Invalid choice. Try again.\n")
