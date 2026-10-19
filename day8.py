# in the lab though BLACK MAMBA 8

expenses = [1200, 450, 250, 200]
total = sum(expenses)
print("My expenses:", total)
print ("Total expenses:", total)
print (total)

# above code is telling you how to print a sum inside a variable. 
# created a variable named expenses, that saves that list and total which uses "sum(..)"
# print statement returns text and the numbers inside the variables
# to just print one number in a bracket -> "print(expenses[0])" - "0" is first index aka "placeholder"
# --> "1"-- would be second, and so forth... 1200 = 0 and 1 = 450
print (expenses[2])


mamba_mode = [81,8,10]
total1 = sum(mamba_mode)
mamba_mode.append (1)
total1 = sum(mamba_mode)
print (total1)

if total1 > 100:
    print ("MAMBA MENTALITY")
elif total1 == 100:
    print ("PERFECT 100")
else:
    print ("Keep Grinding")

# mamba_mode is a variable with a list, total1 is a variable that gives the sum of mamba mode
# to add to a list use the append call, with the added number in parantheses
# whenever you add to a list, you must re-type the "total1" variable along with the sum call in order for ...
# .. append number to be calculated


expenses81 = [24,8,10]
total81 = sum(expenses81)
print (total81)

expenses81.append (100)
total81 = sum(expenses)

if total81 > 200:
    print ("You still think Lebron better than me?")
elif total81 == 200:
    print ("Meet me in the gym @ 5 youngblood")
else:
    print ("Yall cant stop the mamba")

# exercise showing what I leaarned on day 8, created own variables with Kobe Trash talk 
