#day 6 expense analyzer 

name = input ("Enter your name: ")

income = float (input("Enter your monthly income:"))
savings_goal = float(input("Enter your monthly savings goal:"))
rent = float (input("Enter your monthly rent:"))
food = float (input("Enter your food expenses:"))
transportation = float (input("Enter transportation expenses:"))
entertainment = float(input("Enter entertainment costs:"))

expenses = rent + food + transportation + entertainment
money_left = income - expenses 

print ("\n---Monthly Expense Report---")
print ("name:",name)
print ("motnhly_income:", income)
print ("Total expenses: $ ", expenses)
print ("Money left: $", money_left)

if money_left <0:
    print("You are spending more than your earn!")
elif money_left ==0:
    print("You broke even this month foo!")
else:
    print("You have money left over, go buy a stock ya filthy animal!")

savings_goal1 = float(input("What is your savings goal big dawg?"))


expenses = float(input("what are your monthly expenses?"))
income = float(input("What is your monthly income?"))

money_left = income - expenses

savings_gap = savings_goal1 - money_left
if money_left < savings_goal1:
    print(savings_gap)

if expenses > income * 0.80:
    print("watch the numbers esse!!! you need to cut expenses.")