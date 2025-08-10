lst1=[1,2,3]
lst2=[4,5,6]

rev1=lst1[::-1]
rev2=lst2[::-1]

num1 = int("".join(map(str, rev1)))
num2 = int("".join(map(str, rev2)))

total = num1 + num2

sum_list = [int(digit) for digit in str(total)][::-1]

print("Reversed sum list:", sum_list)