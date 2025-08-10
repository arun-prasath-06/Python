
cart=[ ]

items= int(input("How many item do you want to buy ?"))

for i in range(0,items):
    name = input(f"Enter the item {i+1}:")
    price = float(input(f"Enter the price of {name}:"))
    cart.append((name, price))
total=0
for item, price in cart:
    print(f"{item}:{price}")
    total += price

print( "Total Bill:",total)