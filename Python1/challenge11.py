name = input("Enter the student name :")
sub= int(input("enter the number of subject :"))
total= 0

for i in range(1,sub+1):
    mark= float(input(f"Enter the mark {i}:"))
    total += mark
percent= total / sub

if percent > 90:
    grade = "A"
elif percent >= 75:
    grade ="B"
elif percent >=50:
    grade = "C"
else :
    grade = "F"

print("Student Name :",name)
print("Total Marks :",total)
print(f"Percentage: {percent:.2f}%")
print(f"Grade:{grade}")
