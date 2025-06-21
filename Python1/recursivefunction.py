def fact(n):
    if n==1:
        print(n)
        return(n)
    else:
        print(n)
        return n*fact(n-1)
    
a=int(input("enter a number"))
print(fact(a))
