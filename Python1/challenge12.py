# Step 1: Set default PIN and balance
PIN = "1234"
balance = 5000
attempts = 3

# Step 2: PIN verification
while attempts > 0:
    user_pin = input("Enter your PIN: ")
    if user_pin == PIN:
        print("Login successful!\n")
        
        # Step 3: ATM Menu
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            
            choice = input("Enter choice: ")
            
            if choice == "1":
                print(f"Your balance is ₹{balance}")
            
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                balance += amount
                print(f"₹{amount} deposited. New balance: ₹{balance}")
            
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                if amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"₹{amount} withdrawn. New balance: ₹{balance}")
            
            elif choice == "4":
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid choice!")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN! {attempts} attempt(s) left.")

if attempts == 0:
    print("Card blocked due to too many wrong attempts.")
