name = input ("What is your name?")
monthly_income = float(input("What is your monthly income?"))
monthly_expenses = float(input("What are your monthly expenses?"))
money_left = monthly_income - monthly_expenses

if money_left >= 1000:
    print ("you're doing good ya filthy animal!")
    # first message
elif money_left >= 500:
    print ("you need to cut expenses foo!!!")
    # second message
else:
    print ("get your stuff together!!!!")
    #third message

#Q stay in the pocket my guy