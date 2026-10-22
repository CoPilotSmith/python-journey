#day 10 in the lab !

expenses = [1200,450,250,200]

for expense in expenses:
        if expense > 500:
                print ("High Expense Detected:", expense)

## code above creates a for loop for the list in the variable named expense. 
## the if statement checks the list for number greater than 500
## print the statement, follwed by a comma w/ expense variable
## Remember if you put that colon --> : the next line must be indented

high_expenses_count = 0
for expense in expenses: 
        if expense >500:
                high_expenses_count += 1

print (high_expenses_count)

# variable high_expenses_count is started at zero, the for loop checks through the variable named expenses
# for numbers greater than 500, if the counter finds a number greater, it will move the expense count 
# variable up by one number 

print(sum(expenses))
print(len(expenses))

average = sum(expenses) / len(expenses)
print(average)

# the variable average calls the sum function, and the length function and divides them using the /

high_81expense_count = 0 
for expense in expenses: 
        if expense > 500:
                high_81expense_count += 1
print (high_81expense_count)

# created a variable named high_expense_count , the 'for' loop checks the expenses list for
# any number greater than 500, it will move the variable 'high_expense_count up by 1

print ("Total Expense:", sum(expenses))
print ("Average Expense:", average)
print ("High Expenses:", high_81expense_count)

print ("Number of Expense:", len (expenses))

# First print statement, the first one prints Total Expense combined with the sum of the expenses list 
# Second print statement prints the 'average variable' that we created earlier by using sum and len function 
# Third print statement prints 'High expenses' with the high_expense_count --> counter 
# Fourth print statement prints the number of expenses in the list















        

