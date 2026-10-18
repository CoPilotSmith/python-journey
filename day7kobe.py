def calculate_expenses(rent,food,entertainment,transportation):
    total = rent + food + entertainment + transportation
    return total 
rent = int(input("Enter your rent:"))
food = int(input("What are your food expenses?:"))
entertainment = int(input("Enter enterainment cost:"))
transportation = int(input("Enter monthly transportation cost:"))

kobe_bryant = calculate_expenses(rent,food,entertainment,transportation)

def money_left (income,expenses):
    total =  income - expenses 
    return total 
income = int(input("What is your monthly income?:"))
savings_goal = int(input("What is your savings goal?:"))

savings = money_left (income,kobe_bryant)

if savings >= savings_goal:
    print ("You reached your savings goal!")
else:
    print ("get back in the lab esse, get the money!")

def calculate_expenses(rent,food, transportation, entertainment):
    total = rent + food + transportation + entertainment
    return total 
rent = int(input("What is your monthly rent?:"))
food = int(input("Enter food expenses:"))
transportation = int(input("enter transportation costs:"))
entertainment = int(input("enter monthly subscriptions:"))












