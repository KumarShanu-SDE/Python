student_grades = {}

while True:
    print("\nOptions:")
    print("1. Add new student")
    print("2. Update existing student")
    print("3. Print all students")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade
        print("Student added.")
    
    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")
    
    elif choice == '3':
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
