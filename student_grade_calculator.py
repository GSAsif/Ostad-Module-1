# Student Grade Calculator

name = input("Enter student name: ")

total_marks = 0

for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i}: "))
    total_marks += mark

average = total_marks / 3

if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print(f"""
Student Name: {name}
Total Marks: {total_marks}
Average: {average:.2f}
Grade: {grade}
""")