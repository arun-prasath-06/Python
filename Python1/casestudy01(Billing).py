Name=input("Enter your Name")
Amount=float(input("Enter your bill amount"))
if Amount > 1000:
    discount=Amount * 0.10
elif Amount > 500 and Amount <= 1000:
    discount= Amount * 0.05
else:
    print("No Discount Applied")
final_amount=Amount - discount
print(f"\nHello {Name}")
print(f"your final bill amount {final_amount} and discount is {discount}")
print("thanks for shoping visit us again")

    