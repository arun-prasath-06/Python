cart=[]
total_amount=0
item=int(input("How many items are you buying?"))
for i in range(0,item):
    name=input(f"Enter name of item {i+1}:")
    quantity=int(input("Enter quantity:"))
    price=int(input("Enter price per unit:"))
    item_total= quantity * price
    total_amount += item_total
    cart.append((name,quantity,price,item_total))
print("Bill Summary")
for item in cart:
    name,quantity,price,item_total = item
    print(f"{name}-{quantity} x {price}={item_total}")
print("---------------------------")
print(f"Total AMount:{total_amount} ")