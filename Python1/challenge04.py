user_name="admin"
user_password=1234
attempt=0
max_attempt=3

while attempt < max_attempt:
    username=input("username:")
    password=int(input("password:"))
    
    if username == user_name and password == user_password:
        print(f"login successfull welcome {username}")
        break
    else:
        attempt +=1
        print("Incorrect credentials.")
        if attempt < max_attempt:
            print(f"Attemps left:{max_attempt-attempt}")
        else:
            print("Account locked too many failed attempt")