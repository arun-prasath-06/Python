num=int(input("ENter a Number"))
def Check_even_odd(num):
    if num % 2 ==0:
        print(f"{num} is a Even number")
    else:
        print(f"{num} is a odd number")
Check_even_odd(num)

def check_pos_neg(num):
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a Negative number")
    else:
        print(f"{num} is zero")
check_pos_neg(num)