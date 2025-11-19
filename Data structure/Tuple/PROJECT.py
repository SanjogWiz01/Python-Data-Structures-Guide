# student_record_tuple_project.py
# A small tuple-based project for managing student records
print("Welcome to the Student Record Management System!\n")
students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    students.append((name, age, marks))
    print(f"\n✅ {name}'s record added successfully!\n")

def display_students():
    if not students:
        print("\n⚠️ No records found.\n")
        return
    print("\n🎓 Student Records:")
    print("-" * 35)
    for s in students:
        print(f"Name: {s[0]}, Age: {s[1]}, Marks: {s[2]}")
    print("-" * 35, "\n")

def search_student():
    name = input("Enter name to search: ")
    found = False
    for s in students:
        if s[0].lower() == name.lower():
            print(f"\n✅ Found: Name: {s[0]}, Age: {s[1]}, Marks: {s[2]}\n")
            found = True
            break
    if not found:
        print("\n❌ Student not found.\n")

def topper():
    if not students:
        print("\n⚠️ No records to analyze.\n")
        return
    top = max(students, key=lambda s: s[2])
    print(f"\n🏆 Topper: {top[0]} with {top[2]} marks\n")

def average_marks():
    if not students:
        print("\n⚠️ No records to calculate average.\n")
        return
    avg = sum(s[2] for s in students) / len(students)
    print(f"\n📊 Average Marks: {avg:.2f}\n")

while True:
    print("===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Display All")
    print("3. Search Student")
    print("4. Topper")
    print("5. Average Marks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        topper()
    elif choice == '5':
        average_marks()
    elif choice == '6':
        print("\n👋 Exiting... Goodbye!\n")
        break
    else:
        print("\n❌ Invalid choice. Try again.\n")
# End of student_record_tuple_project.py