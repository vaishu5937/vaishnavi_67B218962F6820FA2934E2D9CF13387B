class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa, reverse=True)

# Test the function with different input lists of students
students = [
    Student("Alice", "1", 9.5),
    Student("Bob", "2", 9.0),
    Student("Charlie", "3", 8.5),
]

sorted_students = sort_students(students)
for student in sorted_students:
    print("Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")