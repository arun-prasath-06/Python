lst=[]

for i in range(1,6):
    num = float(input (f"Enter the input {i}:"))
    lst.append(num)
largest= max(lst)
print(f"The largest number is:",largest)