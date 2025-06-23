def fact(n):
    if n==1:
        return(n)
    else:
        print(n)
        return n*fact(n-1)
    
a=int(input("enter a number"))
print(fact(a))
