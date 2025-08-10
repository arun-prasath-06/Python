'''Welcome to Python ATM
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter amount to deposit: 2000
Deposited successfully! New balance: ₹12000

Enter your choice: 2
Enter amount to withdraw: 5000
Withdrawn successfully! Remaining balance: ₹7000

Enter your choice: 3
Your balance: ₹7000

Enter your choice: 4
Thank you for using Python ATM!'''
balance = 10000
while True:
    print("\nWelcome to Python ATM")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice=input("Enter the choice:")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited successfully! New balance: ₹{balance}")
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawn successfully! Remaining balance: ₹{balance}")
    elif choice == "3":
        print(f"Your balance: ₹{balance}")

    elif choice == "4":
        print("Thank you for using Python ATM!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
