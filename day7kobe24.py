def calculate_expenses(rent,food, transportation, entertainment):
    total = rent + food + transportation + entertainment
    return total 
rent = int(input("What is your monthly rent?:"))
food = int(input("Enter food expenses:"))
transportation = int(input("enter transportation costs:"))
entertainment = int(input("enter monthly subscriptions:"))

black_mamba = calculate_expenses (rent,food,transportation,entertainment)

def money_left (income,expenses):
    total = income - expenses
    return total
income = int(input("What is your monthly income?:"))
savings_goal = int(input("What is your monthly savings goal?:"))

savings = money_left (income,black_mamba)

if savings >= savings_goal:
    print ("you met your savings goal el chapo jr!!")
elif savings > 0:
    print ("get to it my boy, need more money!!")
else:
    print ("we gotta get more pesos, dinero, chedda!")
