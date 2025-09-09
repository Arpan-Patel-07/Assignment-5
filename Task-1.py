student_marks = {
    "Alice": 88,
    "Bob": 76,
    "Priya": 92,
    "David": 95,
    "Catherine": 81
}

student_name = input("Enter the name of the student to find their marks: ").strip().title()


if student_name in student_marks:
    
    marks = student_marks[student_name]
    print(f"{student_name}'s marks: {marks}")
else:
    print("Student not found")