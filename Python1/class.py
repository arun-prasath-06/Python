class Bank_Account:
    customer_name=""
    balance = 0.0
    account_number= 0
    def __init__(self,customer_name,balance,account_number):
     print("constructor")
     self.customer_name=customer_name
     self.balance=balance
     self.account_number=account_number
    def __str__(self):
       return(self.customer_name)
Bank=Bank_Account("Arun",5000000,5698)
print(Bank.customer_name,Bank.balance,Bank.account_number)
print(Bank)
"""Bank_Account.customer_name= "Arun"
Bank_Account.balance=500000000
Bank_Account.account_number= 58
print(Bank_Account.customer_name,"\n",Bank_Account.balance,"\n",Bank_Account.account_number)"""