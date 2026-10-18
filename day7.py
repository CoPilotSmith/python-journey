def greet(name):
    print("whats good,", name)
greet("Smitty")

def calculate_expenses(rent,food,transportation, entertainment):
    total = rent + food + transportation + entertainment
    return total 
print (calculate_expenses(1200,450,250,200))


def calculate_money_left(income,expenses):
    money_left_total = income - expenses
    return money_left_total
print(calculate_money_left(3500,2100))

kobe = calculate_expenses(1200,450,250,200)
money_left = calculate_money_left(3500, kobe)

print (money_left)






    



