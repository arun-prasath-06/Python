emp_name=input("enter a name:")
emp_salary=float(input("enter your salary:"))
HRA= emp_salary * 0.20
DA=emp_salary * 0.10
gross=HRA + DA + emp_salary
print(f"Basic salary:{emp_salary}")
print(f"HRA (20%):{HRA}")
print(f"DA (10%):{DA}")
print(f"Gross salary:{gross}")
