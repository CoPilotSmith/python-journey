#part 2 of day 8 really a whole new challenge, using functions from Day 7 

def calculate_money_left (income,expenses):
    money_left81 = income - expenses 
    return money_left81

kobe81 = calculate_money_left (3500,2100)
print (kobe81)

# above is the "money left function"
# accepts income and expenses 
# kobe81 is a variable telling that function to use 3500 and 2100 as the income and expenses

def calculate_savings_gap (savings_goal, money_left):
    total = savings_goal - money_left
    return total 

olympic10  = calculate_savings_gap (2000,1400)
print (olympic10)

# above is a function named "calculate savings gap" it accepts two parameters savings_goal and money_left 
# the colon at the end makes the next lines indented and apart of the function
# olympic10 is a variable that uses 2000 as the savings goal, & 1400 as the money left
# print (olympic10) returns 600 as the total 


def check_savings_status (money_left1):
    return money_left1

game7 = check_savings_status(2500)

if game7 >= 2000:
    print ("Mamba MODE!! Savings goal reached!")
else:
    game7 < 2000
    print ("Youre not there yet, keep grinding")

