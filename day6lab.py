#day 6 expense analyzer 

name = input ("Enter your name: ")

income = float (input("Enter your monthly income:"))
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
print ("Moeny left: $", money_left)

if money_left <0:
    print("You are spending more than your earn!")
elif money_left ==0:
    print("You broke even this month foo!")
else:
    print("You have money left over, go buy a stock ya filthy animal!")
    