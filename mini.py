name = input("What is your name?")
monthly_income = float(input("What is your monthly income?"))
monthly_expenses = float(input("What are your monthly expenses?"))

money_left = monthly_income - monthly_expenses

if money_left >= 1000:
    print("you're doing good, " + name + ".")
else:
    print("you need to chill, watch your spending " + name + "!")
