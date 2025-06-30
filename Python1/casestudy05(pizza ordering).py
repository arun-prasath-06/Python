prices={
    "S":150,
    "M":200,
    "L":250
}
total=0
Num=int(input("How many pizzas do you want to order?"))
cart=[]
for i in range(1,Num + 1):
    size=input(f"Enter size of pizza {i}(S/M/L):")
    if size in prices:
     price=prices[size]
     total+=(price)
     size_full={"S":"small","M":"medium","L":"Large"}[size]
     cart.append(f"pizza{i}:{size_full}-{price}")
    else:
     print("invalid size")
     cart.append(f"pizza {i}:Invalid entry")
for i in cart:
  print(i)
print(total)
print(size_full)
print(prices["S"])