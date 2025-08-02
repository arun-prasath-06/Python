a=int(input("Enter number"))
for i in range(0,a):
    for j in range(i,a):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(i,1,-1):
        print("/",end=" ")
    print()