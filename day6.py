#Day 6 THE MAN WITH THE PLAN! DOING N,UMB,ERS

name = input("what is your name?")
print ("Welcome to the lab,", name)

salary =int(input("Enter your monthly salary:"))
print(salary * 12)

def calculate_annual_salary(monthly_salary):
    annual_salary = monthly_salary * 12
    return annual_salary 

result = calculate_annual_salary(5000)
print(result)