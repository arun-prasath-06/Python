num=int(input("Enter number of students"))
students=[]
for i in range(0,num):
    name=(input(f"enter name of the student{i+1}:"))
    marks=[]
    for j in range(0,3):
        mark=float(input(f"Enter the marks{j+1}:"))
        marks.append(mark)
    average=sum(marks)/3
    status="pass" if average >= 40 else "Fail"
    student = {
        "name": name,
        "marks": marks,
        "average": average,
        "status": status
    }
    students.append(student)
    print("--Students Report--")
    for s in students:
         print(f"Name: {s['name']}")
         print(f"Marks: {s['marks']}")
         print(f"Average: {s['average']:.2f}")
         print(f"Status: {s['status']}")
         print("---------------------")