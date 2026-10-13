name = input("What is your name vato?")
income = float(input("What is your monthly income boss?"))
expenses = float (input("What are your expenses this month?"))
savings_goal = float (input("How much dinero you trying to save guey?"))

savings = income - expenses


if savings >= savings_goal:
    print ("Lemme hold something till tomorrow, " + name + ", you met the savings goal! :)")
else:
    print ("Save that money foo, stay locked in to that goal, " + name + "!")