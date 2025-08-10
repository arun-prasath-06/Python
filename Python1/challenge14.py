'''Enter number of students: 3
Enter name: John
Enter marks: 85
Enter name: Mary
Enter marks: 92
Enter name: Alex
Enter marks: 48

Student Report:
Name     Marks   Grade
John     85      B
Mary     92      A
Alex     48      F'''
student= int(input("Enter numbr of students :"))
report=[ ]
for i in range(0,student):
    name= input("Enter name:")
    marks= int(input("Enter marks:"))
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"
    report.append((name,marks,grade))
print("\nStudent Report:")
print("Name | Marks | Grade")
for name, marks, grade in report:
    print(f"{name}    | {marks}     | {grade}")

